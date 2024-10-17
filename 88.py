#another way to join 2list
#is by appending all the items from list2 into list1,one by one!

#append list2 into list1?

list1=["a","b","c"]

list12=[1,2,3,4]

for x in list12:
    list1.append(x)

print(list1)