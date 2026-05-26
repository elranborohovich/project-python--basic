name = input("enter your name: ")
length = len(name)
if length < 4:
    print("too short")
elif length < 9:
    print("ok")
else:
    print("too long")