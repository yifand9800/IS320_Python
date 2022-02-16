"""HW4 Q2 app, 01/27/22, created by Yifan Dai.

Computes and displays tax (float)
inputs: income(float), married status (string), number of exemptions claimed (integer)
submit outputs: tax (float)
summary outputs: number of married taxpayers (integer), number of unmarried taxpayers (integer), average tax (float)
"""

# global
num_married = 0
num_single = 0
total_tax = 0.0
total_taxpayers = 0

# functions
def compute_marital_status(s):
    global num_married, num_single, total_tax, total_taxpayers
    if s == 'y':
        marital_status = 'married'
    else:
        marital_status = 'single'
    
    return marital_status

def compute_total_exemption(status, exemptions):
    global num_married, num_single, total_tax, total_taxpayers
    
    # update number of single or married taxpayers
    if status == 'married':
        exem_rate = 500.0
        num_married = num_married + 1 
    else: # single
        exem_rate = 375.0
        num_single = num_single + 1

    # compute total exemptions
    total_exemption = exemptions * exem_rate

    # update total counts of taxpayers
    total_taxpayers = total_taxpayers + 1

    return total_exemption

def compute_taxable_income(inc, totalexem):
    global num_married, num_single, total_tax, total_taxpayers

    taxable_income = inc - totalexem

    return taxable_income

def compute_tax_rate(taxable, status):
    global num_married, num_single, total_tax, total_taxpayers

    if status == 'married':
        # compute tax rates depends on taxable amount
        if taxable > 150000.0:
            tax_rate = 0.30
        else:
            tax_rate = 0.20
    else: # single
        if taxable > 100000.0:
            tax_rate = 0.18
        else:
            tax_rate = 0.15
    
    return tax_rate

def compute_tax(tr, taxable):
    global num_married, num_single, total_tax, total_taxpayers

    # compute tax
    tax = tr * taxable

    # update total tax
    total_tax = total_tax + tax

    return tax 

# main
def submit():
    global num_single, num_married, total_tax, total_taxpayers

    # inputs
    income = float(input('Enter your income: >>'))
    marital = input('Married or not (y for yes, n for no): >>')
    num_exemp = int(input('Enter numbers of exemptions claimed: >>'))

    # computations
    # 1. compute marital status
    marital_status = compute_marital_status(marital)

    # 2. compute total tax exemption
    total_exemption = compute_total_exemption(marital_status, num_exemp)

    # computes taxable income
    taxable_income = compute_taxable_income(income, total_exemption)

    # 3. compute tax rate
    tax_rate = compute_tax_rate(taxable_income, marital_status)

    # 4. compute tax
    tax = compute_tax(tax_rate, taxable_income)

    # output
    print(tax)


def compute_average_tax():
    global total_tax, num_married, num_single, total_taxpayers

    # compute average tax only if total payers > 0
    if total_taxpayers > 0:
        avg_tax = total_tax / total_taxpayers
    else:
        avg_tax = None 

    return avg_tax

def summary():
    global num_married, num_single, total_tax, total_taxpayers

    # call average tax function
    avg_tax = compute_average_tax()

    # outputs
    if avg_tax is not None:
        print(num_married, num_single, avg_tax)
    else:
        print('No data...')
    

def reset():
    global num_married, num_single, total_tax, total_taxpayers

    num_married = 0
    num_single = 0
    total_tax = 0.0
    total_taxpayers = 0

submit()
submit()
submit()
summary()
reset()


