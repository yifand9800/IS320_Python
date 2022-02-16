"""HW4 Q2 app, 01/27/22, created by Yifan Dai.

input: score (integer)
output when a series of scores have been entered
submit() output: read one score and call another function
summary() outputs: count of grades (integer), average score(float)
"""
# global
count_perfect = 0
count_A = 0
count_B = 0
count_C = 0 
count_D = 0 
count_F = 0
count_grade = 0
total_score = 0.0

# functions
# update counts for grade that a student recieved 
def update_gradecounts(sc):
    global count_perfect, count_A, count_B, count_C, count_D, count_F, count_grade, total_score
    
    if sc >= 90: # grade A
        if sc == 100: # perfect score = 100
            count_perfect = count_perfect + 1
            count_A = count_A + 1
        else:
            count_A = count_A + 1
    elif sc >= 80: # grade B
        count_B = count_B + 1
    elif sc >= 70: # grade C
        count_C = count_C + 1
    elif sc >= 60: # grade D
        count_D = count_D + 1
    else: # grade F
        count_F = count_F + 1

    # update counts of grades and total scores
    count_grade = count_grade + 1
    total_score = total_score + sc 
    return count_perfect, count_A, count_B, count_C, count_D, count_F, count_grade, total_score

# main
def submit():
    global count_perfect, count_A, count_B, count_C, count_D, count_F, count_grade, total_score

    # input
    score = int(input('Enter your score: >> '))

    # call the functionn to update all global variables
    update_gradecounts(score)

# compute average score
def compute_average_score():
    global total_score, count_grade

    avg_score = total_score / count_grade

    return avg_score

def summary():
    global count_perfect, count_A, count_B, count_C, count_D, count_F, count_grade, total_score
    
    # compute average score
    avg_score = compute_average_score()

    # outputs
    print('\nSummary output for above data:\n')
    print(f'Class Average: {avg_score:.2f}\n')
    print(f'Summary of Letter Grades:')
    print(f'A: {count_A:d}\nB: {count_B:d}\nC: {count_C:d}\nD: {count_D:d}\nF: {count_F:d}\nPerfect Scores: {count_perfect:d}')

def reset():
    global count_perfect, count_A, count_B, count_C, count_D, count_F, count_grade, total_score

    count_perfect = 0
    count_A = 0
    count_B = 0
    count_C = 0 
    count_D = 0 
    count_F = 0
    count_grade = 0
    total_score = 0.0

submit()
submit()
submit()
submit()
submit()
submit()
submit()
submit()
submit()
submit()
summary()
reset()