input_file = open("spliteFile.txt","r")
for i in input_file:
    data = i.rsplit()
    print(data[0])