#num = 2

# Iterate 10 times from i = 1 to 10
#for i in range(1, 11):
#   print(num, 'x', i, '=', num*i)

#######################################
List = []
print ("Enter a multiplication table :")
num = int(input())
for i in range(1,num+1):
   smallList = []
   for j in range(1 , i+1):
      smallList.append(i+j)
   List.append((smallList))

print(List)