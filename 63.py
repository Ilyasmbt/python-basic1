#add any iterable

#the extends() method does not have to append lists,
#you can add any iterable object (tuples,sets ,dictonaries etc.).

#add elemnts of a tuple to a list?



thislist =["app","app1","app2","app3"]
thistuple=["app4","app5"]
thislist.extend(thistuple)
print(thislist)