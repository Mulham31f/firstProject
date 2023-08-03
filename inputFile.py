input_file = open("input.txt","r")

for i in input_file:
    if int(i) %2==0:
        print(i)
    