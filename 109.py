#using asterisk(*)
#if the num of variables is less than the num of values,
#
#you can addadd an * to the variable name
#and the values will be asigned to their//

#assign the rest of the values as a list called "red":

fruits=("apple","banana","cherry",1,2,3,4)
(x ,y,*red)=fruits
print(x)
print(y)
print(red)