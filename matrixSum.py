m1 = [[1,2,3],
     [4,5,6]]

m2 = [[1,2,3],
     [4,5,5]]

for i in range (len(m1)):
    for j in range(len(m1[0])):
        sum = m1[i][j]+m2[i][j]
        print(sum)
            


