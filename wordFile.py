inputFile = open("word.txt","r")

for i in inputFile:
    wordsplit = i.rsplit()
    numberlist = float(wordsplit[0])
    numberlist.sort()
    print(numberlist,numberlist[-1])
    
   
#         word =word.strip("?/*")
#         print(word)