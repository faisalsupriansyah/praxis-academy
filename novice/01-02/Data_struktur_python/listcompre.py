print('squares')
squares = []
for x in range(10):
    squares.append(x**2)

print((squares))

print('combs')
combs = []
for x in [1,2,3]:
   for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
print(combs)

print('vec')
vec = [-4, -2, 0, 2, 4]
newlist = [x*2 for x in vec]
print(newlist)

newlist = [[x for x in vec if x >= 0]]
print(newlist)

newlist = [abs(x) for x in vec]
print (newlist)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
newlist = [weapon.strip() for weapon in freshfruit]
print(newlist)

vec = [[1,2,3], [4,5,6], [7,8,9]]
newlist = [num for elem in vec for num in elem]
print(newlist)

from math import pi
newlist = [str(round(pi, i)) for i in range(1, 6)]
print(newlist)