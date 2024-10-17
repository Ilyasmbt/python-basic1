#you can use index number {0]
# to be sure the arguments are placed in the correct placeholders:



quantity=3
itemno =567
price=49.95
myorder = "i want to pay{2} dollars for{0} piecees of item {1}."
print(myorder.format(quantity,itemno,price`))