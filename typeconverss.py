#implicit_typeconversion
int_a=100
float_b=200.12
ans=int_a+float_b
print(ans)
print("data type: ", type(ans))
ans2=int_a+int(float_b)
print(ans2)

str="300"
ans3=int_a+int(str)
print(ans3)