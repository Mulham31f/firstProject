
for i in range(1,101):
    result = 0 
    
    for j in range(1,i):
        if i%j ==0:
            result +=j
    if i == result:
        print(i)
  
    
    
