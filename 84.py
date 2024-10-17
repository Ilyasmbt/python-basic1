#perform a case-insensitive sort of the list:

friends=["Adil","ABI",'ajanaya','apu',"ammu"]
friends.sort(key=str.lower)

print(friends)
#the key parameter is set to str.lower,
#which means that the list will be sorted based
#on the lowercase version of each string elemeents