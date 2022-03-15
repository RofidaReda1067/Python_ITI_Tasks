#Write a function which has an input of a string from user then it
#will return the same string reversed.
def reverseStr(s):
   if len(s)==1:
       return s
   else:
       return reverseStr(s[1:]) + s[0]
s="rofidareda"
print("the ordered string is : ",end=" ")
print(s)

print("the reversed order is : ",end=" ")
print(reverseStr(s))
#-1