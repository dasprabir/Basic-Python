a = set()
a.add(10)
a.add(20)


for x in a:
    print(a)
    
given_list = [1, 1, 2 ,2 , 2, 4]

new_set = set()

for x in given_list:
    new_set.add(x)
    
print(new_set)

new_list1 = list()
for x in new_set:
    new_list1.append(x)
    
print(new_list1)


givenlist = [1, 3, 4, 1, 3]
new_set2 = set()
for x in givenlist:
    new_set2.add(x)
    
total = 0
for x in new_set2:
    total += x
    
print(total)