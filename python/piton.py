x = [89,42,56,65,78,12,45,63,76,27]
print(f"unsorted array 1: {x}")
y = [15,79,35,16,84,26,38,45,72,11]
print(f"unsorted array 2: {y}")

x.sort()
print(f"sorted array 1: {x}")

def bubbleSort(y):
  n = len(y)
  swapped = False
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if y[j] > y[j + 1]:
        swapped = True
        y[j], y[j + 1] = y[j + 1], y[j]
    if not swapped:
      return

bubbleSort(y)
print(f"Bubble sorted array 2: {y}")