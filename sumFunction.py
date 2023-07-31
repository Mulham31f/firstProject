def total (*args):
    sum = 0
    for i in args:
        sum += i
    print(args)
    return sum

print(total(1,2,3))
