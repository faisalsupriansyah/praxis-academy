import array as arr
a = arr.array("I",[3,6,9])
print (type(a))

x = [] # Empty list
print(type(x))

x1 = [1,2,3]
print(type(x1))

x1 = [1,2,3]
print(type(x1))

x2 = list([1,'apple',3])
print(type(x2))

print(x2[1])

x2[1] = 'orange'
print(x2)

list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['c','o','o','k','i','e']

list_num.append(11) # Add 11 to the list, by default adds to the last position
print(list_num)

list_num.insert(0, 11)
print(list_num)

list_char.remove('o') 
print(list_char)

list_char.pop(-2) # Removes the item at the specified position
print(list_char)

list_num.sort() # In-place sorting
print(list_num)

list.reverse(list_num)
print(list_num)
