#Перевірити якщо в імені є літера 'v' чи велика, чи маленька байдуже.\n
# І вік користувача парний, то написати що він виграв приз, якщо ні, то не виграв.

age = int(input('Please enter your age:'))
name = input('Please enter your name:')
if age % 2 and 'v' not in name:
    print("not win a prize")
else:
    print("win a prize")