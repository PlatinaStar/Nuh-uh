#name = input("please gib nam 🥹\n")
#print(f"Hello, {name}! 🤪")
#print("You have", len(name), "characters in your name (including spaces). 😮")

x = 0
y = 0
op = 0
choice = input("set numbers or input? 1/2\n")
if len(choice) == 1:
  if choice == "1": 
    x = 9
    y = 5
    op = '+'
  elif choice == "2":
    try:
      x = float(input("gib x: "))
      y = float(input("gib y: "))
      op = input("gib operation sign ( + ; - ; * ; ** ; / ; % ): \n")
    except Exception:
      print("There was an Error in input")
      raise
  if y == 0 and op == '/' or y == 0 and op == '%': 
    print("Nuh uh")
    exit()
  match op:
    case '+':
      print(f"you have added {x} and {y} which equals {x + y}")
    case '-':
      print(f"you have subtracted {x} and {y} which equals {x - y}")
    case '*':
      print(f"you have multiplied {x} by {y} which equals {x * y}")
    case '**':
      print(f"you have made {x} to the power of {y} which equals {x ** y}")
    
    case '/':
      print(f"you have divided {x} by {y} which equals {x / y}")
    case '%':
      print(f"you have divided {x} by {y} and this remains: {x % y}")
else:
  print("Nuh uh")

print("\nNumbers from one to ten:")
for i in range(1, 11):
  print(i)

print("\nEven numbers from two to ten")
h = 0
while h <= 10:
  if h % 2 == 0 and h != 0:
    print(h)
  h += 1

print("\nAdded numbers from one to ten")
u = 0
for i in range(1, 11):
  u += i
print(u)

print("\nMultiplied numbers from one to five")
m = 1
n = 1
while m <= 5:
  n *= m
  m += 1
print(n)



#nice