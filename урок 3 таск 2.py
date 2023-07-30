def valid_phone_number(input_string):
    if len(input_string) != 10 or not input_string.isdigit():
        return False
    return True

phone_number = input("Введите номер телефона (10 цифр): ")

if valid_phone_number(phone_number):
    print("Верный формат номера телефона.")
else:
    print("Неверный формат номера телефона. Пожалуйста, введите 10 цифр.")
