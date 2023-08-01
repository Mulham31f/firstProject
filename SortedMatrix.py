
dec = {1:{"name":"john","age": 27,"sex":"Male"},
       2:{"name":"Marie","age": 22,"sex":"Female"},
       3:{"name":"Marie","age": 23,"sex":"Female"}}

sort_orders = sorted(dec.items(), key=lambda x:x[1]['age'])

print(sort_orders)
