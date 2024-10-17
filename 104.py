#append() method

#convert the tuple into a list li list,add "orange",and
#conert it back into a tuple?

fruits=("apple","banan","cherry")
y=list(fruits)
y.append("orange")
fruits=tuple(y)
print(fruits)