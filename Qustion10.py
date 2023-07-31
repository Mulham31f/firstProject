n = int(input ("please enter the n: "))
value = ["hello","pytho","rat","cat","thonnny"]
new_list = []
for i in value:
        if len(i)>n:
          new_list.append(i)
print(new_list)