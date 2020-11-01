import pyttsx3
import speech_recognition as sr

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

def listen(s):
    say(s)
    print(s)
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognizing")
            text = r.recognize_google(audio)
            print(text)
            return(text)
        except:
            print("Can you say that again?")
            exit(0)

r = sr.Recognizer()
engine = pyttsx3.init()

a = int(listen("Enter a number:"))
b = int(listen("Enter another number:"))
sign = input(say("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division\n"))

print("a =",a)
say("a = "+str(a))

print("b =",b)
say("b = "+str(b))

print("sign =",sign)
say("sign = "+sign)

#by default print have end="\n" we have changed end=" "
print("\n",a,sign,b,"=",end=" ")
say(str(a)+sign+str(b)+"=")
#if else ladder to determine which sign
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