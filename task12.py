# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

summ = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))
for x in range(summ):
    for y in range(product):
        if summ == x + y and product == x * y:
            print(f"первое число = {x}, второе число = {y}")
            