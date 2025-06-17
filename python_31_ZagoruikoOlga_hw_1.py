#  Task-1. Запросіть у користувача ім'я та місячну зарплату в доларах та виведіть їхню
#  річну зарплату в тисячах доларів.

# name=input('Input name: ')
# salary_per_month=int(input('Input salary per month: '))
# salary_per_year=salary_per_month*12/1000
# print(f"{name}'s annual salary is {salary_per_year} thousand(ths) dollars ")


# Task-2. Запросіть ціле число і виведіть True, якщо це парне число діапазоні від 100 до 999,
# інакше - «False».

# I-option

# number=int(input ("Input integer number: "))
# if (number >= 100 and number <= 999) and number%2 == 0:
#     print(True)
# else:
#     print(False)

# II-option

# number=input ("Input integer number: ")
# if number.isdigit():
#     int_number=int(number)
#     if (int_number >= 100 and int_number <= 999) and int_number % 2 == 0:
#         print(True)
#     else:
#         print(False)
# else:
#     print("Input correct number!")

#Task-3. Як вхідні дані візьмемо ціле число; Це число від 101 до 999, а його остання цифра не дорівнює нулю.
# Виведіть число, що складається з чисел першого у зворотному порядку.

# number=int(input ("Input integer number: "))
# if (101 <= number <= 999) and number%10!= 0:
#     reverse_str=str(number)[::-1]
#     reverse_number=int(reverse_str)
#     print(reverse_number)
# else:
#     print("Input correct number!")


# Task-4. Запитайте два цілих числа та виведіть:
#a. Їхню суму
# b. Їхня різниця
# c. результат множення
# d. Результат поділу першого на друге
# e. Залишок від поділу першого на друге
# f. True, якщо перше число більше або дорівнює другому, інакше False

first_number=int(input ("Input first integer number: "))
second_number=int(input ("Input second integer number: "))

print(f"Sum: {first_number+second_number}")
print(f"Subtraction: {first_number-second_number}")
print(f"Production: {first_number*second_number}")
print(f"Division: {round((first_number/second_number),2)}")
print(f"Residual from division: {first_number%second_number}")
print(f"Fist number >= Second number? {first_number>=second_number}")
