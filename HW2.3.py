# Додати прінти чи є введений вік парним, чи непарним.
age = input("enter age: ")
age = int(age)
if age >= 100:
    print("the user is deceiving us")
elif age >= 18:
    print("ok")
else:
    print("not ok")
if age % 2:
    print("not double number")
else:
    print("double number")