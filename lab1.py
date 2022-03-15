string = input("Please Enter your words here")
vowel = 0
string.lower()

for i in string:
    if(i =='a' or i =='e' or i =='i' or i =='o' or i == 'u'):
        vowel = vowel+1

print("The total number of vowels =", vowel)