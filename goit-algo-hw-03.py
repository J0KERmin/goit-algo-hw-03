# 1:
from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        current_date = datetime.today()
        
        # Розрахунок різниці між поточною датою та заданою датою
        delta = current_date - date_obj
        
        # Повернення різниці у днях як ціле число
        return delta.days
    except ValueError:
        # Виняток, який виникає, якщо рядок дати не відповідає формату 'РРРР-ММ-ДД'
        print("Неправильний формат дати. Введіть дату у форматі РРРР-ММ-ДД.")
        return None

# Приклад використання функції
date = input('Введіть дату в форматі РРРР-ММ-ДД: ')
days = get_days_from_today(date)
if days is not None:
    print("Кількість днів від заданої дати до поточної:", days)

# 2:
import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних параметрів
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    
    # Генеруємо унікальні випадкові числа
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))
    
    # Повертаємо список відсортованих чисел
    return sorted(list(numbers))

# Приклад використання функції
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))

# 3:
import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та "+"
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Якщо номер не містить міжнародного коду, додаємо "+38"
    if not phone_number.startswith('+'):
        phone_number = '+38' + phone_number
    
    return phone_number

# Приклад використання функції
print(normalize_phone("+38(050)123-32-34"))  # +380501233234
print(normalize_phone("0503451234"))          # +380503451234
print(normalize_phone("(050)8889900"))        # +380508889900
print(normalize_phone("38050-111-22-22"))     # +380501112222
print(normalize_phone("38050 111 22 11"))     # +380501112211

# 4:
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо день народження у datetime об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Перевіряємо, чи день народження вже минув в цьому році
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()
        if birthday_this_year < today:
            # Якщо так, розглядаємо день на наступний рік
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()

        # Визначаємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження відбувається протягом наступного тижня
        if 0 <= days_until_birthday < 7:
            # Перевіряємо, чи день народження припадає на вихідний
            if birthday_this_year.weekday() == 5 or birthday_this_year.weekday() == 6:
                # Якщо так, переносимо дату привітання на наступний понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Додаємо ім'я користувача та дату привітання у список
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "Іван", "birthday": "2024.02.11"},
    {"name": "Петро", "birthday": "2024.02.12"},
    {"name": "Марія", "birthday": "2024.02.15"},
    {"name": "Олена", "birthday": "2024.02.25"},
    {"name": "Андрій", "birthday": "2024.02.22"},
    {"name": "Юлія", "birthday": "2024.02.24"}
]

print(get_upcoming_birthdays(users))


