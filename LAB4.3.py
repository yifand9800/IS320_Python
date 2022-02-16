"""HW4 Q2 app, 01/27/22, created by Yifan Dai.

Computes and displays comission and total pay.
input: weekly sales (float)
submit() outputs: total pay (float), commission if weekly sales over 1000 (float)
summary outputs: number of salespersons (integer), number of salesperson earning commission (integer), average pay (float)
"""

# global
num_sales = 0
num_sales_cm = 0
total_pay = 0.0

# functions
def compute_commission(sale):
    global num_sales_cm

    # initialization
    commission_rate = 0.15

    # computes commission based on weekly sales
    if sale >= 1000.0:
        commission = sale * commission_rate
        num_sales_cm = num_sales_cm + 1
    else:
        commission = 0.0

    return commission

def compute_pay(cm):
    base_salary = 250.0
    pay = base_salary + cm

    return pay

# main
def submit():
    global num_sales_cm, num_sales, total_pay
    #input
    weekly_sales = float(input('Enter the weekly sales: >> $'))

    # computation
    commission = compute_commission(weekly_sales)
    pay = compute_pay(commission)

    # update
    num_sales = num_sales + 1
    total_pay = total_pay + pay

    #outputs (based on the total pay amount)
    if commission > 0.0:
        print(f'The commission is ${commission:.2f}, and the total pay is ${pay:.2f}.')
    else:
        print(f'The total pay is ${pay:.2f}.')

def compute_average_pay():
    global num_sales_cm, num_sales, total_pay

    avg_pay = total_pay / num_sales 

    return avg_pay

def summary():
    global num_sales_cm, num_sales, total_pay
    avg_pay = compute_average_pay()

    # outputs
    print(num_sales, num_sales_cm, avg_pay)


def reset():
    global num_sales, num_sales_cm, total_pay

    num_sales = 0
    num_sales_cm = 0
    total_pay = 0.0

submit()
submit()
summary()
reset()