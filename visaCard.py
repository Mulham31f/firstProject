number = input("please enter the card number :")
length = len(number)

if length ==8 and number[0:4].isdigit() and number[4]==" " and number[5:].isdigit():
    print("valid number")
else:
    print("not valid number")