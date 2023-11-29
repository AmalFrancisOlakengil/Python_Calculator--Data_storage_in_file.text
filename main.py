a = 'yes'
b = 0
history = open('data.txt', 'r')
print('History:')
print(history.read())
while a == 'yes':
  history = open('data.txt', 'a')
  history.write('\n')
  if b == 0:
    A = float(input("Enter a Number: "))
    C = input("Enter the operator: ")
    B = float(input("Enter a Number: "))
    history.write(str(A)+C+str(B))
    
  else:
     C = input("Enter the operator: ")
     c = float(input("Enter a Number: "))
     history.write(C+str(c))
  if C == '+':
    if b == 0:
      result = A + B
    else:
      result += c
  elif C == '-':
    if b == 0:
     result = A-B
    else:
      result -= c
  elif C == '*':
    if b == 0:
     result = A*B
    else:
      result *= c
  elif C == '/':
    if b == 0:
     result = A/B
    else:
      result /= c
  elif C == '%':
    if b == 0:
     result = A%B
    else:
      result %= c
  else:
     print("invalid Operator")
  print('The result is ', result)
  a = input('Enter \'yes\' to continue operation with result \n or \'No\' to discontinue operation with result: ')
  b += 1
