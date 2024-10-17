#customize sort function

#you can also customize your own function by
#using the keyword argument key = function.
#the function will return
#a number that  will be used to sort the list (the lowest number first)

#sort the list based on how close the number is to 50?

#sort the list based on how close the number is to 50?

def myfun(n):
    return abs(n-50)
thislist = [100,33,44,55]
thislist.sort(key=myfun)
print(thislist)


#myfun(100) return abs(100-50)=50
#.myfun(33) return abs(33-50)=22
#.myfun(44) return abs(44-50)=6
#myfun(55) return abs(55-50)=5
#.


#the list is sorted based on these returned values:
#the sorted order of th list will be:
#which corresponds to sorted by the absolutedifference fom 50
