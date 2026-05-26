user_string = input("Enter a string: ")

if user_string [0] == "A":
    user_string = "a" + user_string [1:]
    print("change to a", user_string)
else:
    print("user string is:", user_string)