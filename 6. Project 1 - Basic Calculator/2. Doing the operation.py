a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
sign = input("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division\n")

print("a =",a)
print("b =",b)
print("sign =",sign)

#by default print have end="\n" we have changed end=" "
print("\n",a,sign,b,"=",end=" ")

#if else ladder to determine which sign
if(sign == '+'):
    print(a+b)

elif(sign == "-"):
    print(a-b)

elif(sign == "*"):
    print(a*b)

elif(sign == "-"):
    print(a/b)