
weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in cm: "))

height /=100
BMI = (weight/(height)**2)
 
if BMI <18.5:
         print("Underweight %.2f"%(BMI))
     
elif 18.5<= BMI <=25.0:
    
         print("Normal %.2f"%(BMI))
         
elif 25.0<= BMI <=30.0:
    
         print("Overweight %.2f"%(BMI))
else:
    
         print("obese %.2f"%(BMI))
