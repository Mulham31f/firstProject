messege = input("please enter the messeage :")
uppercase = 0

for char in messege:
    if char.isupper():
        uppercase +=1
print(uppercase)