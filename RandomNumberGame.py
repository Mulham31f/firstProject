import random
a = ""
ansr = False
num1 = random.randint(0, 10)

while(not ansr):

    a =int(input("enter your answer:"))
    print(num1)
    if a == num1:
        print("correct answer")
        ansr = True
        
    elif a < num1:
        print("go upper")
       
    elif a>num1:
        print("go lower")
        
        
