

def average(*numbers):
  sumOfNums = sum(numbers)
  return (sumOfNums / len(numbers))

print (average(2, 4, 6))


def storeValues (**obj):
  print (obj)
  
storeValues(name= "joe", age = 33)


# Flexible returns

def getPoint():
  return (3, 6)

x, y = getPoint()
print(x,y,end=" ", sep=",")


# Lambda Anonymous Functions


def mult(a, b):
  return a * b

def power(a,b):
  return (a ** b)


operator = mult
print (operator(10, 3))


operator = lambda a, b : a + b

print (operator(10, 3))
