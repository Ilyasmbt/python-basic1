

  #without list comprehension
  #you will have to write a for statement with a conditional test inside:

fruits =["apple","banana",'cherry','kiwi']
chandana =[]
for x in fruits:
    if "b" in x:
          chandana.append(x)
print(chandana)





#65235641654165145614561

#using list comprehension

fruits1 = ["apple",'orange',"grapes","mango","kiwi"]
newlist1=[ x for x in fruits1 if "k" in x]
print(newlist1)