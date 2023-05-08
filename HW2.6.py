# Спитати користувача вік, стать та ім'я. Для усіх молодше\n
# 15 ми пишемо що рекомендуємо теніс, для хлопців старше 15 рекомендуємо футбол, \n
# для дівчат баскетбол, але якщо в імені є літера 'c' або 't', друкуємо \n
# що ми не рекомендуємо займатися спортом

age = int(input('Please enter your age:'))
name = int(input('Please enter your name:'))
gender = int(input("Please enter your gender:"))
if "c" in name or "t" in name:
    print("sport not recommended")
elif age <= 15:
    print("tennis")
elif gender == "boy":
    print("football")
elif gender == "girl":
    print("basketball")
else:
    print("sport recommender")