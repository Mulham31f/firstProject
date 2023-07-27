hour1 = int(input("please enter hour1:"))
mint1 = int(input("please enter mint1:"))
hour2 = int(input("please enter hour2:"))
mint2 = int(input("please enter mint2:"))



if hour1 < hour2 :
        print("first time come before ")
elif hour1==hour2:
        if mint1<=mint2:
            print("first time come before ")
        else:
            print("second time come before ")
else:
    print("second time come before ")
    
    