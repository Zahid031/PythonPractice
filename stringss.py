str1="hi"
str2='hello'
print(str1+'\n'+str2)
str3=str1+str2
print(str3)
print(str3[3:-1])
# for i in str3:
#     print(i)
count=0
for i in str3:
    if(i=='l'):
        count+=1

print(count)
default_order='{} {} and {}'.format('Today','is','sunday')
print(default_order)
positional_order='{1} {0} and {2}'.format('is','today','sunday')
print(positional_order)
#string methods
print("hi my name is ZaHid".lower())
print("hi my name is ZaHid".upper())
print("hi my name is ZaHid".find('Is'))
print("hi my name is ZaHid".replace('hi','hello'))