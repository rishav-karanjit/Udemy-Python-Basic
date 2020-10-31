import pyttsx3

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def say(s):
    engine.say(s)
    engine.runAndWait()
    return s

engine = pyttsx3.init()


a = int(input(say("Enter a number:")))

b = int(input(say("Enter another number:")))


sign = input(say("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division\n"))

print("a =",a)
say("a = "+str(a))
print("b =",b)
say("b = "+str(b))
print("sign =",sign)
say("sign = "+sign)

print("\n",a,sign,b,"=",end=" ")
say(str(a)+sign+str(b)+"=")

if(sign == '+'):
    print(add(a,b))
    say(add(a,b))

elif(sign == "-"):
    print(sub(a,b))
    say(sub(a,b))

elif(sign == "*"):
    print(mul(a,b))
    say(mul(a,b))

elif(sign == "/"):
    print(div(a,b))
    say(div(a,b))