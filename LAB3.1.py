"""HW3 Q1 app, 01/19/22, created by Yifan Dai.

Computes and displays tax (float)
inputs: marital status (strings), income (float)
outputs: tax (float)
"""

#functions
def compute_tax_rate(status, salary):
    if status == 'y': #married
        if salary > 200000: 
            tax_rate = 0.20
        else: #at or below 200,000 dollars
            tax_rate = 0.15
    else: #for 'n' = not married
        if salary > 100000:
            tax_rate = 0.15
        else: #at or below 100,000 dollars
            tax_rate = 0.10
    return tax_rate

#main
#inputs
marital_status = input('Married or not? (y or n) >>')
income = float(input('Enter your income: >>'))

#initializations
#computations
#1. compute tax rate
tax_rate = compute_tax_rate(marital_status, income)
#2. compute tax
tax = income * tax_rate 

#output
print(f'Your tax is ${tax:.2f}.')