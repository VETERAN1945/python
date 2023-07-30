def valid_phone_number(input_string):
    if len(input_string) != 10 or not input_string.isdigit():
        return False
    return True

phone_number = input("Введите номер телефона (10 цифр): ")

if valid_phone_number(phone_number):
    print("Верный формат номера телефона.")
else:
    print("Неверный формат номера телефона. Пожалуйста, введите 10 цифр.")
#task2
import random

def math_quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    expression = f"{num1} {operator} {num2}"
    user_answer = input(f"Чему равно {expression}? ")

    try:
        expected_answer = eval(expression)
        user_answer = int(user_answer)

        if user_answer == expected_answer:
            print("Правильно! Ответ верный.")
        else:
            print(f"Неправильно! Правильный ответ: {expected_answer}.")
    except:
        print("Некорректный ввод. Пожалуйста, введите число.")

math_quiz()