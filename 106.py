#remove items
#note: you cannot remove items in a tuple.


#tuples are unchangeable,so u cannot remove items from it,
#but u can use the same workaround as we used for changing
#and adding tuple items:

#convert the tuple into a list,remove"apple",
#and convert it back into a tuple?

fruits=("apple","banana","cherry")
y=list(fruits)
y.remove("apple")
fruits=tuple(y)

print(fruits)