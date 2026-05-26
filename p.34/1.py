# גיל המשתמש

age = int(input("enter your age: "))

# תיקון ערכים לא תקינים

if age < 0:
 print("0")  
elif age > 120:
 print("120")
    
    # בדיקה לפי טווחי גיל

if age <=18:
  print("teenager")
else:
    print("adult")
    