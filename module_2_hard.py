from random import randint

n = randint(3, 20)
print(f"Сгенерированное число: {n}")

result = ""

for i in range(1, 21):
    for j in range(i + 1, 21):
        if n % (i + j) == 0:
            result += str(i) + str(j)

print(f"Нужный пароль: {result}")
