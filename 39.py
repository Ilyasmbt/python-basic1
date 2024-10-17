#the format ()method takes unlimited num of arguments
#and are placed into the respective placeholders:


quantity =3
itemno=456
price=45.50

myorder ="I want {} pieces of item{}cfor {}dollars."
print(myorder.format(quantity,itemno,price))