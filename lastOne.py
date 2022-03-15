#Word guessing game (hangman)
#guessing_Word="BioTechnology"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_Of_Guesses = False

#while guess != guessing_Word and not (out_Of_Guesses):
#    if guess_count < guess_limit:
#      guess = input("Enter your Guessing:")
#      guess_count +=1
#    else:
#        out_Of_Guesses = True
#if out_Of_Guesses:
#    print("out_Of_Guesses,oops you lose!")
#else:

#    print("YOU WINNN!")
########################################
import random
#name = input ("what is your name? player:")

#print("GoodLuck! ", name)


#guessing_Words =["programming", "bioinformatics", "python", "biotechnology", "microbiology","iti"]

#guessing_Words = random.choice(guessing_Words)
#print("GUESS The Character")
#guesses = ''

#turns =5
#while turns >0:
    #failed =0

   # for char in guessing_Words:
  #     if char in guesses :
  #          print(char, end="")
 #       else:
#         print("_")
  #          print(char,end="")

 #           failed += 1

#    if failed ==0:
#        print("YOU WINNNNN!")
#        print("The word is: ", guessing_Words)
#        break

#print()
#guess =input("guess a character:")

#guesses +=guess
#if guess not in guessing_Words:
#    turns -=1

#    print("ooppss!")

  #  print("you have", +turns,  "Try Again")

 #  if turns==0:

#      print("oh noooo, you lose")


#########################################################
import random

wordlist = ['giraffe','dolphin',\
            'pineapple','durian',\
            'blue','purple', \
            'heart','rectangle']

#Obtain random word
randWord = random.choice(wordlist)

#Determine length of random word and display number of blanks
blanks = '_ ' * len(randWord)
print ()
print ("Word: ",blanks)


#Set number of failed attempts
count = 6

#Obtain guess
while True:
    print ()
    guess = input ("Please make a guess: ")
    if len(guess) != 1:
        print ("Please guess one letter at a time!")
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
       print ("Please only guess letters!")

#Check if guess is found in random word
    for letters in randWord:
        if guess == letters:
            letterIndex = randWord.index(guess)
            newBlanks = blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
            print ("Guess is correct!")
        else:
            count -=1
            print ("Guess is wrong! ", count, " more failed attempts allowed.")
    print()
    print("Word: ",newBlanks)