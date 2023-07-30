def greaterNum(n,x,z):
    if n>=x and n>=z:
        return n
    elif x>=n and x>=z:
        return x
    else:
        return z
    
print("the greatest number = ",greaterNum(0,5,1))
    