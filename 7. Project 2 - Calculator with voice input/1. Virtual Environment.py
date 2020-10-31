def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

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
    print(add(a,b))

elif(sign == "-"):
    print(sub(a,b))

elif(sign == "*"):
    print(mul(a,b))

elif(sign == "/"):
    print(div(a,b))