text = input("please enter the message: ")

for letter in text:
    ascii = int(ord(letter)-3)
    print(chr(ascii),end="")