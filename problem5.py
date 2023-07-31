from math import *

a = int(input ("please enter the a: "))
b = int(input ("please enter the b: "))


while b:
    a, b = b , a%b
print(a)

