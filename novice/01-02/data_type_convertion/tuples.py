x_tuple = 1,2,3,4,5
y_tuple = ('c','a','k','e')
print(x_tuple[0])

x_dict = {'Edward':1, 'Jorge':2, 'Prem':3, 'Joe':4}
del x_dict['Joe']
print(x_dict)

print(x_dict['Edward'])

print(len(x_dict))
print(x_dict.keys())
print(x_dict.values())

x_set = set('CAKE&COKE')
y_set = set('COOKIE')

print(x_set)
print(y_set)
print(x_set|y_set)

f = open('file_name', 'w')
