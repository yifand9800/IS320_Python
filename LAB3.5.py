"""HW3 Q2 app, 01/24/22, created by Yifan Dai.

Computes and displays exemption amount (float) and tax (float)
inputs: income(float), married status (string), number of exemptions claimed (integer)
outputs: married status(string), income(float), number of exemptions (integer), tax (float)
""" 
#global
single_count = 0
married_count = 0
total_tax = 0.0
tax_list = []

#functions
def compute_total_exemption(married, exemptions):
    if married:
        exemp_amount = 500.0
    else: #single
        exemp_amount = 375.0

    total_exemption = exemptions * exemp_amount
        
    return total_exemption

def compute_tax_rate(taxable, married):
    if married:
        #compute tax rates depends on taxable amount
        if taxable > 150000.0:
            tax_rate = 0.30
        else:
            tax_rate = 0.20
    else: #single
        if taxable > 100000.0:
            tax_rate = 0.18
        else:
            tax_rate = 0.15

    return tax_rate

def process_input(income, married, num_exemp):
    global total_tax, single_count, married_count, tax_list

    #initializations
    #computations
    #2. compute total tax exemption
    total_exemption = compute_total_exemption(married, num_exemp)
    #computes taxable income
    taxable_income = income - total_exemption
    #3. compute tax rate
    tax_rate = compute_tax_rate(taxable_income, married)
    #4. compute tax
    tax = tax_rate * taxable_income

    #update total tax
    total_tax = total_tax + tax
    if married:
        married_count = married_count + 1
    else:
        single_count = single_count + 1
    tax_list.append(tax)

    return total_exemption, taxable_income, tax_rate, tax

#main
def submit():
    global total_tax, single_count, married_count, tax_list
#inputs
    income = float(input('Enter your income: >>'))
    if income <= 0.0:
        print(f'{income:.2f} should have been positive . Try again.')
        return 

    married = int(input('Married or not (1 for yes, 0 for no): >>'))
    num_exemp = int(input('Enter numbers of exemptions claimed: >>'))
    if num_exemp < 0 or num_exemp > 3:
        print('Exemptions count must be in range 0...3')
        return 

    marital_status, total_exemption, taxable_income, tax_rate, tax = process_input(income, marital, num_exemp)

    #outputs
    print(f'{marital_status:s}\nincome {income:.2f}\n{num_exemp:d} exemptions\ntax is {tax:.2f}')

def compute_avg_tax():
    global total_tax, married_count, single_count

    if total_tax > 0.0:
        average_tax = total_tax / (married_count + single_count)
    else:
        average_tax = None

    return average_tax

def summary():
    global total_tax, married_count, single_count
    average_tax = compute_avg_tax()
    if average_tax is None:
        print('No data...')
    else:
        print(average_tax, married_count, single_count)

def reset():
    global total_tax, married_count, single_count, tax_list
    single_count = 0
    married_count = 0
    total_tax = 0.0
    tax_list = []

def display():
    global tax_list
    print('--------------')
    print('----tax----')
    print('--------------')
    for tax in tax_list:
        print(tax)
    print('--------------')

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
