# Author: David Gilkeson

# Program for generating prime numbers

primes = []                               # Empty list created
upto = 101

numbers  = range(2,upto)                  # Numbers is in range from 2 to 100

for number in numbers:
  print(number, end= " ")
  isPrime = True
  
  # Check to see if it is a prime
  for divisor in range (2, number):
    if number % divisor == 0:
      isPrime = False
      break
  
  # If it is still a prime
  if isPrime:
    primes.append(number)
    
print(primes)
