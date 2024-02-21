arr = [[65,21,75],[45,31,78],[35,12,69]]

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
  
def partition(unsortedArray, low, high):
  pivot = unsortedArray[high]
  i = low - 1
  for j in range(low, high):
    if unsortedArray[j] <= pivot:
      i = i + 1
      (unsortedArray[i], unsortedArray[j]) = (unsortedArray[j], unsortedArray[i])
  (unsortedArray[i + 1], unsortedArray[high]) = (unsortedArray[high], unsortedArray[i + 1])
  return i + 1
 
def quick_sort(unsortedArray, low, high):
  if low < high:
    part = partition(unsortedArray, low, high)
    quick_sort(unsortedArray, low, part - 1)
    quick_sort(unsortedArray, part + 1, high)

def quick_sort_2d(unsortedArray):
  for i in range (len(unsortedArray)):
    quick_sort(unsortedArray[i], 0, len(unsortedArray[i]) - 1)

def print_2d_matrix(array):
    for i in range(len(array)):
        print(array[i])

print("Our array")
print_2d_matrix(arr)

print("\nBubble sorted array")
print_2d_matrix(bubble_sort(arr))

print("\nInsertion sorted array")
print_2d_matrix(insertion_sort(arr))

print("\nSelection sorted array")
print_2d_matrix(selection_sort(arr))

print("\nQuick sorted array")
quick_sort_2d(arr)
print_2d_matrix(arr)
