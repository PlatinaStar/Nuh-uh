x = [86,5,158,42,36,67,48,54,168,75]
y = [75,16,25,45,87,213,12,4,87,423]

print("Array:", x)

print("Numbers in positions '5' and '10' in array:", x[4], x[9])

print("Length of array x:", len(x))

x.reverse()
print("Reversed array:", x)

x.sort()
print("Sorted array:", x)


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
print(f"Bubble sorted array: {y}")
