""" Y Dai Question 1 app, 02/10/22.
inputs:
# of jobs (int)
income (float)
# of children (int) 
Is Married?  (int)
Is Student? (int)

compute and display tax as a output in submit: 
tax (float) format:  Your estimated taxes due are: $XXXX

output in summary: 
taxpayer count (int) average tax for students (float) non-student counts (int)
single students (int) married students (int) 

global variable: 
married students (int)  single students (int) student counts (int) 
non-student counts (int) total tax from student (float) tax list (list)
"""

# global variables
married_student_count = 0
single_student_count = 0
student_count = 0
non_student_count = 0
total_student_tax = 0.0
tax_list = []

# functions
def count_regular_exemptions(married, job, income, student):
    regular_exem = 1
    if job == 0: #no job
        regular_exem += 1
    elif job == 1: # one job
        if married or (not married and student):
            regular_exem += 1
    else: # more than one jobs
        if income < 1500.0:
            regular_exem += 1
    
    return regular_exem

def count_child_exemptions(income, num_child):
    if income < 70000.0:
        child_exem = num_child * 4
    else:
        child_exem = num_child // 2
    
    return child_exem

def compute_taxable_income(income, child_exem, regular_exem):
    child_amount = 1000.0 * child_exem
    regular_amount = 2000.0 * regular_exem
    exemp_amount = child_amount + regular_amount
    taxable_income = income - exemp_amount

    return taxable_income

def compute_tax_rate(taxable_income, married):
    if married:
        if taxable_income <= 78000.0:
            tax_rate = 0.10
        else: #above
            tax_rate = 0.15
    else: #not married
        if taxable_income <= 38000.0:
            tax_rate = 0.10
        else: #above
            tax_rate = 0.15
    
    return tax_rate

def compute_deduction(income, student):
    #initialization
    deduction = 0.0
    if student and income < 57000.0:
            deduction = 3000.0
    elif student and income < 80000.0:
            deduction = 2000.0
 
    return deduction

def process_input(num_job, income, num_child, married, student):
    global married_student_count, single_student_count, student_count, total_student_tax, tax_list
    
    regular_exem = count_regular_exemptions(married, num_job, income, student)
    child_exem = count_child_exemptions(income, num_child)
    exemption_count = regular_exem + child_exem
    taxable_income = compute_taxable_income(income, child_exem, regular_exem)
    tax_rate = compute_tax_rate(taxable_income, married)
    tax =  taxable_income * tax_rate
    deduction = compute_deduction(income, student)

    #update tax by subtracting any dedecution amount from tax
    tax -= deduction

    #set tax to 0.00 if tax < 0
    if tax < 0.00:
        tax = 0.00

    #update total taxes from students
    if student: 
        total_student_tax += tax

    #update tax list
    tax_list.append(tax)
    
    return regular_exem, child_exem, exemption_count, taxable_income, tax_rate, deduction, tax

def submit():
    global married_student_count, single_student_count, student_count, total_student_tax, tax_list, non_student_count
    #input
    num_job = int(input('# of jobs: >> '))
    income = float(input('income: >> '))
    num_child = int(input('# of children >> '))

    #validation
    if num_child < 0:
        print('number must be zero or above, please try again.')
        return
    
    married = int(input('Is Married? (1 for yes, 0 for no): >> '))
    student = int(input('Is Student? (1 for yes, 0 for no): >> '))

    # validation and update
    if student == 1:
        student_count += 1
        if married:
            married_student_count += 1
        else:
            single_student_count += 1
    elif student == 0:
        non_student_count += 1
    else: #not 1 or 0 => invalid input
        print('Please enter 1 or 0 to valid your answer.')
        return

    regular_exem, child_exem, exemption_count, taxable_income, tax_rate, deduction, tax = process_input(num_job, income, num_child, married, student)

    print(f'Your estimated taxes due are: ${tax:.2f}')
    
def compute_average_student_tax():
    global total_student_tax, student_count

    if total_student_tax > 0.00:
        avg_student_tax = total_student_tax / student_count
    else:
        avg_student_tax = None
    
    return avg_student_tax

def summary():
    global married_student_count, single_student_count, non_student_count, student_count, total_student_tax
    avg_student_tax = compute_average_student_tax()

    if avg_student_tax is not None:
        print(f'Taxpayer counts: {non_student_count + student_count:d}, married student counts: {married_student_count:d}, single student counts: {single_student_count:d}, non student counts: {non_student_count:d}\nAverage tax for students: ${avg_student_tax:.2f}')
    else:
        print('No data...')

def display():
    global tax_list
    print('--------------')
    print('----tax-------')
    print('--------------')
    for tax in tax_list:
        print(tax)
    print('--------------')

def reset():
    global married_student_count, single_student_count, student_count, total_student_tax, tax_list, non_student_count

    single_student_count = 0
    married_student_count = 0
    student_count = 0
    non_student_count = 0
    total_student_tax = 0.0
    tax_list = []

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





