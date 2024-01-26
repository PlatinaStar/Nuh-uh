yellow = [58, 98, 12, 43, 69, 14]

def bubble_sort(yellow):
  n = len(yellow)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if yellow[j] > yellow[j + 1]:
        yellow[j], yellow[j + 1] = yellow[j + 1], yellow[j]
  return yellow

print(yellow)
print(bubble_sort(yellow))


def selection_sort(green):
  n = len(green)
  for i in range(n):
    min = i
    for j in range(i+1, n):
      if green[j] < green[min]:
        min = j
    green[i], green[min] = green[min], green[i]
  return green

green = [57, 97, 11, 42, 68, 13]
print(green)
print(selection_sort(green))

def insertion_sort(hollow):
  for i in range(1, len(hollow)):
    key = hollow[i]
    j = i - 1
    while j >= 0 and key < hollow[j]:
      hollow[j + 1] = hollow[j]
      j -= 1
    hollow[j + 1] = key
  return hollow

hollow = [8, 5, 3, 48, 6, 27]
print(hollow)
print(insertion_sort(hollow))