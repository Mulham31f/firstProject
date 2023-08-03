input_file = open("input.txt","r")
total = 0
count = 0
for i in input_file:
    print(i)
    total=total+float(i)
    count+=1
print("---"*5)
print("Total:",total)
avrg = total/count
print("Average:",avrg)
