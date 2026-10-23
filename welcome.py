print("Приветствуем в FitLife MVP")
user_name = input("Как вас зовут? - ")
print("Рады познакомиться!!!", user_name) 
user_age = int(input("Сколько вам лет? - "))
user_weight = float(input("Укажите пожалуйста ваш вес в кг: "))
user_height = float(input("Укажите ваш рост в метрах как пример 1.57: "))
# Расчет индекса массы тела
bmi = round(user_weight / user_height ** 2, 1)
# 30мл воды на 1кг массы общепринятая норма 
water_per_kg = 30
water_ml = user_weight * water_per_kg 
water_1_liters = 1000
water_1 = round(water_ml / water_1_liters, 1)
# Для удобства чения кода, обратился к ии практикума
report = (
    f"Отчет для пользователя: {user_name}, {user_age}\n" 
    f"Твой индекс тела: {bmi}\n" 
    f"Рекомендованная норма воды в литрах: {water_1} л. в день"
)
print(report)
print("Расчет окончен. Будьте здоровы!")