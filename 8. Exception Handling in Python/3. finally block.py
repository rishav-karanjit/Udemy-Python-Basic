def abcd():    
    a = int(input("Enter a integer"))
    b = int(input("Enter a integer"))
    try:
        print(a/b)
        return 1
    except:
        print("Exception occured")
        return -1
    finally:
        print("Ending the program")

print(abcd())
