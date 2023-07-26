gender = input("please enter gender m or f :")
age = int(input("please enter your age:"))
if gender == 'm'or 'M' :
    if 24<= age <= 30:
        print("you are accept for the job")
    else:
        print("you are male but not accepted")
elif gender == 'f'or 'F':
     print("you are woman and we need male ")
     
else:
        print ("your gender is not accepted")
    