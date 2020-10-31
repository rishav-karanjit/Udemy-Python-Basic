# try:
#     statement #exception could occur
# except:
#     statement #excuted after exception occurs

# a/b

a = int(input("Enter a integer"))
b = int(input("Enter a integer"))
try:
    print(a/b)
except:
    print("Exception occured")

print("Ending the program")