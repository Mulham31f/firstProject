import random

ansr = ""
while( ansr != "done"):

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print(num1, "+",num2)
    sum_1 = str(num1+num2)
    ansr =input("enter your answer:")
    if ansr == sum_1:
        print("correct answer")
    elif ansr == "done":
        print("goodbye!")
       
    else:
        print("wrong answre")
        
        
    

