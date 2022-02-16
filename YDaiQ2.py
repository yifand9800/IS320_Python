""" Y Dai Question  2, 02/10/22.
inputs: number of books ordered (int)   status - online or offline (int)

compute the order price inclusive of shipping/tax

output in submit: order price (float)  inclusive of shipping/tax (float)
output in summary: average revenue for online orders (float)   average tax collected (float)

global variables: 
number of online orders (int) number of offline orders (int)
total revenue (float) total tax (float) list of order prices (list)
""" 

#global
num_online = 0
num_offline = 0
total_online_revenue = 0.0
total_tax = 0.0
order_price_list = []


#functions
def compute_order_price(books, status):
    global total_online_revenue

    #initialization
    unit_price = 15.0
    #compute order price
    order_price = unit_price * books

    #update total revenue for online orders
    if status:
        total_online_revenue += order_price

    #update order price lists
    order_price_list.append(order_price)

    return order_price

def compute_ship_cost(status, books):
    global num_online

    #initialization
    ship_rate = 0.0

    #computes shipping cost
    if status: # online order
        num_online += 1 # update number of online orders
        if books <= 10:
            ship_rate = 0.25
        else:# number of books > 10
            ship_rate = 0.30

    ship_cost = ship_rate * books

    return ship_cost


def compute_tax(status, order_price):
    global num_offline, total_tax

    #initialization
    tax_rate = 0.07
    tax = 0.0

    #compute tax for offline orders
    if not status: 
        num_offline += 1 #update counts
        tax = tax_rate * order_price

    #update total tax
    total_tax += tax

    return tax

def process_input(books, status):
    global num_offline, num_online, total_online_revenue, total_tax, order_price_list

    #1. computes order price
    order_price = compute_order_price(books, status)

    #2. computes shipping cost
    ship_cost = compute_ship_cost(status, books)

    #3. computes tax
    tax = compute_tax(status, order_price)

    return  order_price, ship_cost, tax

def submit():
    global num_offline, num_online, total_online_revenue, total_tax
    
    #inputs
    books = int(input('Enter the number of books ordered: >> '))

    #validation: must be a positive number
    if books <= 0:
        print(f'Your number of books must be positive. Please try again.')
        return 

    status = int(input('Enter 1 for online, 0 for offline: >> '))

    #validation: should be 1 or 0
    if status != 1 and status != 0:
        print('Please enter 1 for online and 0 for offline. Try again.')
        return

    #call process input
    order_price, ship_cost, tax = process_input(books, status)

    #update order price inclusive of shipping/tax
    #outputs
    if status: #online
        order_price += ship_cost
        print(f'{books:d} online : ${order_price:.2f}')
    else: #offline
        order_price += tax
        print(f'{books:d} offline : ${order_price:.2f}')

def compute_avg_revenue():
    global num_online, total_online_revenue
    
    #compute average revenue only when have online orders
    if num_online > 0:
        avg_revenue = total_online_revenue / num_online
    else:
        avg_revenue = None 

    return avg_revenue

def compute_avg_tax():
    global num_offline, total_tax

    #compute average tax only when have offline orders
    if num_offline > 0:
        avg_tax = total_tax / num_offline
    else:
        avg_tax = None

    return avg_tax

def summary():
    global num_offline, num_online, total_online_revenue, total_tax
    
    #computes average revenue for all orders
    avg_revenue = compute_avg_revenue()
    avg_tax = compute_avg_tax()

    #outputs
    if avg_revenue is not None and avg_tax is not None:
        print(f'Your average revenue for online orders is ${avg_revenue:.2f}, and average tax is ${avg_tax:.2f}.')
    else:
        print('No data...')

def display(): #exlcusive of shipping/tax
    global order_price_list

    print('-------------------')
    print('----order price----')
    print('-------------------')
    for order_price in order_price_list:
        print(order_price)
    print('-------------------')

def reset():
    global num_offline, num_online, total_online_revenue, total_tax, order_price_list

    num_online = 0
    num_offline = 0
    total_online_revenue = 0.0
    total_tax = 0.0
    order_price_list = []

#main loop    
quit = False # => not quit
while not quit:  #some condition holds
    print('1. Submit 2. Summary 3. Reset 4. Display 5. Quits')
    choice = int(input('Enter 1, 2, 3, or 4 >>'))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for new series...')
    elif choice == 4:
        display()
    elif choice == 5:
        #quit the app => exit the loop => condition failed
        quit = True
    else:
        print('Invalid choice!')

print('Goodbye!')