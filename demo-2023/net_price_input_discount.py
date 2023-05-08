data = int(input("Enter Price : "))
price = data
discount = int(input("Enter discount percentage : "))
discount_on_price = price * discount / 100
net_price = price - discount_on_price
print('Price : ', price)
print('Discount : ', discount)
print('Discounted price :', discount_on_price)
print('Net Price : ', net_price)