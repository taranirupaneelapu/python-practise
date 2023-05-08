#Accept basic salary and display net salary after including 30% HRA and 20% DA

salary = int(input("Enter Salary : "))
HRA = salary * 30 / 100  #can also write this formula as HRA = salary * 0.30
DA = salary * 20 / 100
net_salary = salary + HRA + DA
print(net_salary)