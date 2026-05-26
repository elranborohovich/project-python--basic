# כתיבת סיסמא
password = input("Enter password:")

# בדיקה אם הסיסמא קצרה מ‑8 תווים
if len(password) < 8:
    print("ERROR: Password must be at least 8 characters long.")

# בדיקה על האות הראשונה
elif password[0] not in ["Z", "C"]:
    print("ERROR: Password must start with 'Z' or 'C'.")

# בדיקה שהתו האחרון הוא $
elif password[-1] != "$":
    print("ERROR: Password must end with '$'")
else:
    print("strong password")
    
    