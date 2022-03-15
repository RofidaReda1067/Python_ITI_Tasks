Arr=[]
num = int(input("please enter number of elements:"))
for i in range(0, num):
    element = int(input())

    Arr.append(element)

print(Arr)

newArr = sorted(Arr)
print(newArr)

newArr2 = sorted(Arr, reverse=True)
print(newArr2)