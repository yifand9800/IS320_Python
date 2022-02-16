"""HW3 Q1 app, 01/24/22, created by Yifan Dai.

Computes and displays the gross pay (float), the taxes (float) and the net pay (float).
inputs: number of hours worked (float)
outputs: gross pay (float), taxes (float), net pay (float)
"""

#function
#computes gross pay
def compute_gross_pay(hrs):
    basic_rate = 10.0
    overtime_rate = 1.5 * basic_rate
    max = 40.0
    excess = hrs - max
    if excess <= 0.0: #regular  hours
        gross_pay = basic_rate * hrs
    else: #over 40 hours
         #overtime
        gross_pay = (basic_rate * max) + (overtime_rate * excess)
    return gross_pay

#computes taxes
def compute_tax(gross):
    first = 300.0
    second = 150.0
    tax_rate_1 = 0.15
    tax_rate_2 = 0.20
    tax_rate_3 = 0.25
    if gross <= first: #first $300
        tax = gross * tax_rate_1
    elif gross <= (first + second): #gross pay <= $450
    #computes include first $300 and next $150 with two tax rates respectively
        left = gross - first #computes how much left for 20% tax rate
        tax = (first * tax_rate_1) + (left * tax_rate_2)
    else: #gross pay > $450
        left = gross - (first + second) #computes how much left for 25% tax rates
        tax = (first * tax_rate_1) + (second * tax_rate_2) + (left * tax_rate_3)
    return tax

#main
#inputs
hours = float(input('Enter hours you worked: >>'))

#computations
gross_pay = compute_gross_pay(hours)
tax = compute_tax(gross_pay)
net_pay = gross_pay - tax

#outputs
print(f'Your gross pay is ${gross_pay:.2f}, tax is ${tax:.2f}, net pay is ${net_pay:.2f}.')
