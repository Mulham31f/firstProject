def calculateAvergae(value):
    total = 0
    for i in range(len(value)):
        total +=value[i]
        avrg = total/(len(value))
    return avrg

list = [60,70,90,100,76]
avrg1= calculateAvergae(list)
print(avrg1)
    