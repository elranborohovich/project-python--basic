# בחירת מספר חיובי

number = int(input("enter a positive number: "))

# בדיקה שהמספר חיובי
if number > 0:
    for i in range(1, number + 1):
        print(i)
else:
     print("ERROR: The number must be positive.")

