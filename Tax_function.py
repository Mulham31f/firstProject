def addTax(price,rate):
    tax = price *rate /100
    price = price+tax
    return price

total = 5
print(addTax(total,7.5))