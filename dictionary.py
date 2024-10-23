dict1={1:"hi",2:"hello",3:"good"}
print(dict1)
print(dict1[1])
print(dict1.get(4))
#update a value
dict1[1]="Update hi"
print(dict1[1])
dict1.pop(1)
print(dict1)
print(dict1.popitem())
del dict1[2]
print(dict1)
dict1[5]="Updating"
print(dict1)
dict1.clear()
print(dict1)
del dict1

#creating a dictionary using comprehension
dict1={x:x*x for x in range(1,5)}
print (dict1)
print (1 in dict1)
#traversing
for i in dict1:
    print(dict1[i])
print(len(dict1))
print(sorted(dict1))
