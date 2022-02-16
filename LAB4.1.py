""" HW4 Q app, 01/27/22, created by Yifan Dai.

Computes and displays tax (float)
inputs: order options (strings), books (integer)
submit outputs: order price (float), shipping/tax (float)
summary output: number of offline (integer), number of online (integer), average revenue (float)
"""

# global
num_online = 0
num_offline = 0
total_revenue = 0.0
order_count = 0

# function
def compute_order_price(bks):
    global num_offline, num_online, total_revenue, order_count

    # initializations
    unit_price = 15.0
    # compute order price
    order_price = unit_price * bks
    # update total revenue
    total_revenue = total_revenue + order_price

    return order_price

def compute_shipping_cost(opt, bks):
    global num_offline, num_online, total_revenue, order_count

    # initializations
    variable_rate = 0.25
    flat_rate = 5.0
    ship_cost = 0.0

    # computes shipping cost
    if opt == 1: # online order
        num_online = num_online + 1 # update number of online orders
        if bks <= 10:
            ship_cost = variable_rate * bks
        else:# number of books > 10
            ship_cost = flat_rate

    return ship_cost


def compute_tax(opt, bks, price):
    global num_offline, num_online, total_revenue, order_count

    # initialization
    tax_rate = 0.08
    tax = 0.0

    # computes tax
    if opt == 0: # offline order
        num_offline = num_offline + 1 # update number of offline orders
        tax = tax_rate * price

    return tax

# main
def submit():
    global num_offline, num_online, total_revenue, order_count
    
    # inputs
    books = int(input('Enter the number of books ordered: >> '))
    order_status = int(input('Enter 1 for online, 0 for offline: >> '))
    
    # 1. computes order price
    order_price =  compute_order_price(books)
    
    # 2. computes shipping cost
    ship_cost = compute_shipping_cost(order_status, books)

    # 3. computes tax
    tax = compute_tax(order_status, books, order_price)

    # update the number of orders
    order_count = order_count + 1

    # outputs
    print(order_price, ship_cost, tax)

def compute_avg_revenue():
    global num_offline, num_online, total_revenue, order_count
    
    # compute average revenue only when have orders
    if order_count > 0:
        avg_revenue = total_revenue / order_count
    else:
        avg_revenue = None 

    return avg_revenue

def summary():
    global num_offline, num_online, total_revenue, order_count
    
    #computes average revenue for all orders
    avg_revenue = compute_avg_revenue()

    # outputs
    if avg_revenue is not None:
        print(num_online, num_offline, avg_revenue)
    else:
        print('No data...')

def reset():
    global num_offline, num_online, total_revenue, order_count

    num_online = 0
    num_offline = 0
    total_revenue = 0.0
    order_count = 0

submit()
submit()
submit()
summary()
reset()