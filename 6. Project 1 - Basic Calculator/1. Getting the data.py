# input() -> Takes user input in the form of string

a = int(input("Enter a integer:")) #We have changed string to integer because operations like addition cannot be performed in string
b = int(input("Enter a integer:"))

sign = input("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division\n")
#No need to convert sign variable to integer because we don't expect integer in sign

print("a =",a)
print("b =",b)

print("sign =",sign)