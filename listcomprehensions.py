list1=[]
for letter in "Human":
    list1.append(letter)
    print(list1)
list2=[letter for letter in "Human"]
print(list2)
#if comprehension
list3=[letter for letter in "Human" if letter=='H' or letter=='n']
print(list3)
#if else
list4=["even" if i%2==0 else "Odd" for i in range(10)]
print(list4)