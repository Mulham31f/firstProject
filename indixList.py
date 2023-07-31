myList = [3,5,1,7,2,8]
sum = 0

for i in range(len(myList)):
    print(i,myList[i])
print("-"*4)

for i in myList:
    sum +=i
print("=",sum,"the sum of the indix")

