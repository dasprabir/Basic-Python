
a = [ 1, 3, 5, 9, 11 ] # double the elements in list
b = []
b.append(10)
b.append(20)

c = []
for x in a:
    c.append( 2*x )
    
print(c)


# List comprehension

d = [ x*2 for x in a]
print(d)

# [1 ,4 , 9, 16, 25, 36 ]

e1 = []

for x in range(1,7):
    e1.append( x**2 )
    
print(e1)

########################################
p = list(range(6, 0, -1))
l = [ x**2 for x in p ]
print(l)

#################################
f = []

for x in range(6, 0, -1):
    f.append(x**2)
    
print(f)