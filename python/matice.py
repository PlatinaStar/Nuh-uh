array = [[45,74,39,22],[48,64,18,23],[27,53,14,29],[82,47,95,16]]
print(f"Our array: {array}")
print(f"Length of our array: {len(array)}")
print(f"3rd array in our array: {array[2]}")
print(f"2nd number in the 3rd array in our array: {array[2][1]}")
print(f"arrays summed up together: {sum(sum(array,[]))}")

def create_2d_matrix(m,v,n):
    a = []
    for _ in range(n):
        a += [[v] * m]
        v += 1
    
    return a

def print_2d_matrix(array):
    for i in range(len(array)):
        print(array[i])

print("Our 2D matrix:")
print_2d_matrix(array)

print("Created 2D matrix:")
y = create_2d_matrix(3,1,3)
print_2d_matrix(y)

def create_2d_matrix_2(n):
    a = []
    for _ in range(n):
        a += [[[0.] * 4] * 2]
    return a

z = create_2d_matrix_2(5)
print_2d_matrix(z)


