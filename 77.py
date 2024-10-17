#return "orange" instead of "banana"?

fruits = ["apple","banana","cherry",'kiwi',"mango"]
newlist =[x if x != "banana" else "orangee" for x in fruits]
print(newlist)
