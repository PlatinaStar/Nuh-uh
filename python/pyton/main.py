x = [[3, 5, 2, 7], [9, 4, 8, 5], [2, 6, 7, 1]]
print(f"Main array: {x}")
print(f"Length of main array: {len(x)}")
print(f"first item (array) in main array: {x[0]}")
print(f"fourth item inside second item (array) in main array: {x[2][3]}")

def create_2d_matrix(m,v,n):
  a = []
  for _ in range(n):
    a += [[v] * m]
    v += 1
    
  return a

def print_2d_matrix(array):
  for i in range(len(array)):
    print(array[i])
    
print("\nDefined matrix:")

print_2d_matrix(x)

print("\nCreated matrix:")

a = create_2d_matrix(3, 6, 3)
print_2d_matrix(a)