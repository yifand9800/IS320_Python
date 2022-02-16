"""HW3 Q2 app, 01/19/22, created by Yifan Dai.

Computes and displays points (integer)
inputs: name (strings), books (integer)
outputs: name (strings), points (integer)
"""

#inputs
name = input('Enter your name: >>')
num_books = int(input('How many books did you read? >>'))

#initializations
first = 3
second = 6
first_pts = 10
second_pts = 15
last_pts = 20

#computations
if num_books <= first: #number of books <= 3
    points = num_books * first_pts
elif num_books <= second: #number of books <= 6
    left = num_books - first
    points =  (first * first_pts) + (left * second_pts)
else:#number of books > 6
    #points would be 3*10 + 3*15 + (number of books - 6)*20
    left = num_books - second
    points = (first * first_pts) + (first * second_pts) + (left * last_pts)

#outputs
print(f'Member Name: {name:s}\nNumber of books read: {num_books:d}\nPoints earned: {points:d} points')