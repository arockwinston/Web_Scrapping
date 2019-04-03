
#<--------------Dictionary Use case------------>

#---->Add values
checkdic = {}
checkdic["one"] = "Onnu"
checkdic["Two"] = "Rendu"

#---->Seperate the values as list key and list value
list_key = list(checkdic.keys())
list_value = list(checkdic.values())
list_all = list(checkdic)
List2_dictionary = {}
for i,j in list_key,list_value:
    List2_dictionary.update({i:j})
print("United list:",List2_dictionary)

print(list_all)
print(list_key, list_value)
print(checkdic)

#---->Search by Key
str = "three"
checkdic2 = {"one": "uno", "two": "dos", "three": "tres"}
print(checkdic2[str])

#---->Delete the key&value
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
del inventory["apples"]
print(inventory)

#---->Stack operation
buy = 50
inventory["bananas"] -= buy
inventory["pears"] = 0
print(inventory)

#---->Get lenth of the dictionary
print(len(inventory))

#---->Check the by matching the value by itration
for k in inventory:
    if inventory[k] == 0:
        print("The key is:", k)
    else:
        print("Not in :", k)

#---->List of tuples to dictionary
list_tuple = list(inventory.items())  
print(list_tuple)

#---->List of tuples to dictionary
new_dictionary = {}
for i,k in list_tuple:
    if i != None and k != None:
        new_dictionary.update({i:k})
    else:
        print("Fail")
print(new_dictionary)

if "oranges" in new_dictionary:
    print("Yes")
else:
    print("No")

  #<------------------Dictionary----------------->

dic = {"name":"Arock", "seatno":10, "mark":9.5}
print(dic)
print(type(dic)) #To check the type
key = dic.keys() #To get the key values only
value = dic.values() #To get the values of the key
print(key)
print(value)

name = dic.get("name") #Get values by Key
print(name)

dic['mark'] = 9.5 #Alter the values
dicList = dic.items() #To get the list of items
print(dicList)

dic.update({"exam": "Maths"}) #Update the dictionary with new "Key:value"
print(dic)

dic.update({"check": "kkk"})
dic.popitem()  #Pop last updated value
dic.pop("exam") #Pop by key
print(dic)

dic.update({"dept": "csc"})
dic.setdefault("maths", None) #set default value for key
print(dic)

x = ('exam', 'dept', 'sec')
y = 'null'
thisdict = dic.fromkeys(x, y) #Insert more key by default value
print(thisdict)

  