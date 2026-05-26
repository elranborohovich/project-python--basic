# הכנס כתובת מייל
email = input("Enter email address: ")

# בדיקה אם המייל קצר מ‑4 תווים
if len(email) < 4:  # (בדיקה אם האורך קטן מ-4)
    print("ERROR")  # (הדפסת שגיאה)

# בדיקה אם התו הראשון או האחרון הוא '@'
elif email[0] == "@" or email[-1] == "@":  # (בדיקה אם @ בהתחלה או בסוף)
    print("ERROR")  # (הדפסת שגיאה)

# אם שתי הבדיקות עברו — כתובת תקינה
else:
    print("Valid email:", email)  # (כתובת תקינה)
