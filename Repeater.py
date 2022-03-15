#Write a program which repeatedly reads numbers until the user
#enters “done”

#count = 0
#total = 0
#num = 0
#while True:
   # num = input("plz enter your number:")

  #  if num.isdigit():
   #      continue
  #  if num == 'Done':
  #          break

 #   try:
 #       num = (num)
 #   except:
 #      print ('Invalid Input')
 #   continue

#count = count+1
#total = total + num
#print( 'You inputted',count,num)
#print('The total is:',total)
#print ('The average is:',total/count)
###############################################
sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Plz Enter a number: ")
    if (x =="Done"):
     break
    value = int(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input.")
print(sum, count,average)
