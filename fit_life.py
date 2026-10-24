# Проект FitLife - MVP версия 1.0
print("Приветствуем в FitLife MVP")

# 1. Знакомство
user_name = input("Как вас зовут? - ")
user_age = int(input("Сколько вам лет? - "))


# 2. Сбор данных
user_weight = float(input("Укажите пожалуйста ваш вес в кг: "))
user_height = float(input("Укажите ваш рост в метрах как пример 1.57: "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / user_height ** 2, 1)
water_per_kg = 30
water_ml = user_weight * water_per_kg
water_1_liters = 1000


# Подсчет воды: вес * 30 мл
water_1 = round(water_ml / water_1_liters, 1)


# 4. Вывод красивого результата
# Для удобства чтения кода, обратился к ии практикума
print(
    f"Отчет для пользователя: {user_name}, {user_age}\n"
    f"Твой индекс тела: {bmi}\n"
    f"Рекомендованная норма воды в день: {water_1} л.",
)
print("Расчет окончен. Будьте здоровы!")
