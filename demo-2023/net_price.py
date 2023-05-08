# Take price from user and calculate net price with 10% discount
data = int(input("Enter the Price:"))
price = data
discount = price * 10 / 100
net_price = price - discount

# now i want to display price, discount and net_price
print('Price :', price)
print('Discount :', discount)
print('Net Price :', net_price)

