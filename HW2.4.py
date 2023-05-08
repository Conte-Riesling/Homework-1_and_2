#Додати що користувач вводить ще й ім'я. І якщо в імені є літера 'a', \n
# то написати що ми навідь не збираємося його перевіряти.
age = int(input('Please enter your age:'))
name = input('Please enter your name:')
if 'a' in name:
   print("not cheked")
else:
   if age >=18:
       print("verify")
   else:
       print("not verify")
