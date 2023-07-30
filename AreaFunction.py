from math import *

def squr(n):
    area = n*n
    return area

def cyrc(r):
    area = pi*(r**2)
    return area

def rect(n,m):
    area = n*m
    return area

def cyl(r,h):
    area = (2*pi*r)(h+r)
    return area

def tri(n,h):
    area = 0.5*n*h
    return area

n=""
while(n!="Q"):
    n=(input("choose number or Quit ="))
    n = n.upper()
    if n=="1":
        l =int(input("please enter the length ="))
        print(squr(l))
    elif n=="2":
        r =int(input("please enter the radies ="))
        print(cyrc(r))
    elif n=="3":
        x =int(input("please enter the heigth ="))
        y =int(input("please enter the width ="))
        print(rect(x,y))
    elif n=="4":
        a =int(input("please enter the radies ="))
        h =int(input("please enter the height ="))
        print(cyl(a,h))
    elif n=="5":
        o =int(input("please enter the width ="))
        l =int(input("please enter the height ="))
        print(tri(o,l))
        
    
    


    