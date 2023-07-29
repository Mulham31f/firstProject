number = input("please enter the number :")
length = len(number)

if length ==12 and number[0]=="+" and number[1:4]=="968" and number[4:].isdigit():
    print("valid number")
else:
    print("not valid number")
