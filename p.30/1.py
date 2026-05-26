# בחירת מספר

number = int(input("Enter a number: "))

# בדיקה אם המספר חיובי או שלילי

if number>0:
    print("Positive")
elif number==0:
    print("Zero")
else:
    print("Negative")
    
    # בדיקה אם המספר זוגי או אי זוגי
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")