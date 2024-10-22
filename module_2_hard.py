from random import randint

# Генерация случайного числа от 3 до 20
n = randint(3, 20)
print(f"Сгенерированное число: {n}")

# Инициализация пустой строки для пароля
result = ""

# Поиск пар чисел
for i in range(1, 21):
    for j in range(i + 1, 21):
        if n % (i + j) == 0:  # Проверка кратности
            result += str(i) + str(j)  # Добавление пары в результат

# Вывод результата
print(f"Нужный пароль: {result}")