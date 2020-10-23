a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
sign = input("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division\n")

print("a =",a)
print("b =",b)
print("sign =",sign)

print(a,sign,b,"=",end=" ")
if(sign == "+"):
    print(a+b)

elif(sign == "-"):
    print(a-b)

elif(sign == "*"):
    print(a*b)

elif(sign == "/"):
    print(a/b)