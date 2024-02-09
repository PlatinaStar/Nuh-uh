import random

arr = [[1,5,82,6,12],[4,18,5,46,7],[2,65,7,4,32],[95,12,35,1,6]] #1

print(f"Our array: {arr}")

print(f"Length of array: {len(arr)}") #2

print(f"Third array in main array: {arr[2]}") #3

print(f"Second number in third array in main array: {arr[2][1]}") #4

add = []

for i in range(4):
    add += arr[i]

print(f"arrays added together: {add}")  #5

def print_2d_matrix(array):
  for i in range(len(array)):
    print(array[i])

print_2d_matrix(arr) #6

a = [[0.]*4]*2
print(a)
for y in range(1):
    a[y][2] = 2.

print(f"Created array with changed number: {a}") #7

b = [[0.]*4 for _ in range(5)]
print("Created array with 4 columns and 5 rows:") #8
print_2d_matrix(b)

b[1][1] = 4.
print("Changed number in array") #9
print_2d_matrix(b)