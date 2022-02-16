"""HW3 Q2 app, 01/19/22, created by Yifan Dai.

Computes and displays tax (float)
inputs: order options (strings), books (integer)
outputs: order price (float), shipping/tax (float)
"""

#functions
def compute_cost(opt, bks, price):
    variable_rate = 0.25
    flat_rate = 5.0
    tax_rate = 0.08
    if opt == 1: #online order
        if bks <= 10:
            cost = variable_rate * bks
        else:#number of books > 10
            cost = flat_rate
    else: #0 = offline order
        cost = price * tax_rate
    return cost

#main
#inputs
num_books = int(input('How many books ordered? >>'))
order_options = int(input('Enter 1 for onlline order, 0 for offline order: \n>>'))

#initialization
unit_price = 15.0

#computation
#1. compute order price
order_price = unit_price * num_books
#2. compute shipping/tax cost
cost = compute_cost(order_options, num_books, order_price)

#outputs
print(f'Your order price is ${order_price:.2f}, inclusive of shipping/tax ${cost:.2f}.')