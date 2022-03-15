def FizzBuzzGame(num):
  if ((num % 3 == 0) and (num % 5 == 0)) :
     print("fizz buzz")
  elif (num % 5 == 0):
    print("buzz")
  elif (num % 3 == 0):
    print("fizz")
  else:
    print("None")

FizzBuzzGame(5);
