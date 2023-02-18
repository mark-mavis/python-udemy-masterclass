
#These operators apply to any sequence type in python

Itemlist = "item1", "item2", "item3", "item4", "item5"

print(Itemlist[3])          #item4
print(Itemlist[3][0:3:1])   #ite

#Concatenators
print(str(Itemlist[0][0:4:2]) + str(Itemlist[1][0:4:1]))

#Multiplication
print(Itemlist[3] * 5)

#Check if a string is a substring of another

today = "Tuesday"

print("day" in today)
print("fri" in today)
print("thur" in today) 
print("item3" in Itemlist)