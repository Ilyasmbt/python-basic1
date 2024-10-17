#global variable
#create a variable outside of a function, and
#use it inside the function & outside the function

y ="awesome" #scope of y is global

def fun():
    print("python is "+ y)

fun()
print(y)