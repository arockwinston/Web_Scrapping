nums = [45, 67, 87, 87, 54]
print(nums)  #List
print(nums[1]) #List with index
print(nums[1:3]) #List with range index
print(nums[-2]) #Negative index range

stringlist = ["Arock", "Winston", "Is", "Not", "Arock"]
print(stringlist) #list of strings

values = ["Arock", 87, 9.01]
print(values) #list of multiple values

mil = [nums, stringlist, values]
print(mil) #List of list

nums.append(99) #Append values in the list
print(nums)

cont = stringlist.count("Arock") #Returns the number of times the value exist in the list
print(cont)

ind = nums.index(87)
print(ind) #Print the index of the value: If similar values in the  list then it return the index of the first value

cop = nums.copy()
print(cop)   #Copy the list to another variable

cop.clear()  #Clear the list values
print(cop)

nums.insert(6, 100) #Insert value by index value
print(nums)   

nums.pop() #Pop without an index value
print(nums)

nums.pop(2) #Pop with an index value
print(nums)

nums.remove(87) #Remove element from the list
print(nums)

del nums[0] #delete by index value
print(nums)

nums.extend([24,65,76]) #extent the list by adding more value into it
print(nums)

nums.reverse() # Reverse the list element
print(nums)

nums.sort() #Sort the element in the list
print(nums)
