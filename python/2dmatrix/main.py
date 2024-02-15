arr = [[65,21,75],[45,65,78],[35,12,69]]

def bubble_sort(unsortedArray):
  n = len(unsortedArray)
  for k in range(n):
    for i in range(len(unsortedArray[k]) - 1):
        for j in range(len(unsortedArray[k]) - i - 1):
            if unsortedArray[k][j] > unsortedArray[k][j + 1]:
                unsortedArray[k][j], unsortedArray[k][j + 1] = unsortedArray[k][j + 1], unsortedArray[k][j]
  return unsortedArray

def selection_sort(unsortedArray):
  n = len(unsortedArray)
  for k in range(n):
    for i in range(len(unsortedArray[k])):
        min = i
        for j in range(i+1, n):
            if unsortedArray[k][j] < unsortedArray[k][min]:
                min = j
            unsortedArray[k][i], unsortedArray[k][min] = unsortedArray[k][min], unsortedArray[k][i]
  return unsortedArray

def insertion_sort(unsortedArray):
  for k in range(1, len(unsortedArray)):
    for i in range(1, len(unsortedArray[k])):
        key = unsortedArray[k][i]
        j = i - 1
        while j >= 0 and key < unsortedArray[k][j]:
            unsortedArray[k][j + 1] = unsortedArray[k][j]
            j -= 1
        unsortedArray[k][j + 1] = key
    return unsortedArray

def print_2d_matrix(array):
    for i in range(len(array)):
        print(array[i])

print_2d_matrix(arr)

print_2d_matrix(bubble_sort(arr))
