import re
if re.search('hi','hi , my name is zahid'):
    print("yes hi is in the string")
else:
    print("string not available")
allfind=re.findall('hi.','hi how are you hiii')
for i in allfind:
    print(i)
str1="hi this is zahid and i am trying to learn python"
for i in re.finditer('is.',str1):
    lockspan=i.span()
    print(lockspan)
print(str1[lockspan[0]:lockspan[1]])

allfind1=re.findall("..",str1)
for i in allfind1:
    print(i)
