value = [1,2,-3,-5,5]
start = 1
sum = 0

for i in value:
    print(i, end=" x ",)

for i in value:
    start *=i
print(" = ", start)

for i in value:
    if i<0:
        sum+=1
print(sum,"element in the list is negitive")

    
    
    