from math import *

def area(n,side):
    function = (n*(side**2))/(4*tan((pi/n)))
    return function

n = float(input("please enter the number of side :"))
s = float(input("please enter the side :"))
    
print(area(n,s))