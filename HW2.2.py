#Додати до першої умови, якщо вік більше ніж 100, роздрукувати \n
# текст що користувач вводить нас в оману
age = input("enter age: ")
age = int(age)
if age >= 100:
    print("the user is deceiving us")
elif age >= 18:
    print("its ok")
else:
    print("its not ok")