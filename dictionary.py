contacts = {"Fred":7235591, #create new dictionary
            "Mary":3841212,
            "Bob": 3841122,
            "Sarah":728822}
oldContacts = dict(contacts) #duplicates dictionary
print("Fred's number is",contacts["Fred"]) #print the contects of the dictionry
print("--"*10)
#cheak the contects of the dictionry
if "said" in contacts:
    print("said is in the list")
elif "Bob" in contacts:
    print("bob is in the list")
else:
    print("said is not the list")
print("--"*10) 
number = contacts.get("Sarah","Not in my contacts") #contacts.get() give you the value of the contacts
print(str(number))

contacts["Mohammed"] = 9856568
print(contacts)
print("--"*10)
contacts.pop("Bob")
print(contacts)
bobNumber = contacts.pop("Fred")
print(contacts)
print(bobNumber)
print("--"*10)
for i in contacts:
    print(i,contacts[i])
print("--"*10)
for item in contacts.items():
    print(item[0],item[1])
