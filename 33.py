#remove whitespace

#whitespace is the space before and/or after the actual text
#and very often you want to remove this space

#the strip() method removes any whitespace from the beginning or the end:
a="      hello      ,  ilyas!   "
print(a.strip())        #retuens "hello,ilyas
print(a)