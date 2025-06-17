#TASK-1.
# Як вхідні дані запитайте ціле число.
# Якщо воно ділиться на 3, виведіть "foo";
# якщо воно ділиться на 5, виведіть "bar";
# якщо воно ділиться на обидва, виведіть "ham" (а не "foo" або "bar").
while True:
    number=input("Input integer number: ")
    if number.isdigit():
        int_number=int(number)
        break
    else:
        print("Error, input correct number!")

if int_number%3==0 and int_number%5==0:
    print("ham")
elif int_number%3==0:
    print("foo")
elif int_number%5==0:
    print("bar")
else:
    print(f"{int_number} is not divisible by 3 or 5")

#TASK-2.
# Як вхідні дані запитайте два цілих числа та виведіть яке з них менше і яке більше

# while True:
#     number1 = input("Enter an integer number1: ")
#     if number1.isdigit():
#        int_number1 = int(number1)
#        break
#     else:
#         print("Error, enter correct number!")
# while True:
#     number2 = input("Enter an integer number2: ")
#     if number2.isdigit():
#        int_number2 = int(number2)
#        break
#     else:
#         print("Error, enter correct number!")
# if int_number1>int_number2:
#     print("First number is bigger than Second number")
# elif int_number1==int_number2:
#     print("First number is equal to Second number")
# else:
#     print("First number is smaller than Second number")


# #TASK-3.
# Як вхідні дані запитайте три цілих числа і виведіть найменше, середнє та найбільше.
# Припустимо, всі вони різні
# list_numbers=[]
# while True:
#     number1 = input("Enter an integer number1: ")
#     if number1.isdigit():
#        int_number1 = int(number1)
#        list_numbers.append(int_number1)
#        break
#     else:
#         print("Error, enter correct number!")
# while True:
#     number2 = input("Enter an integer number2: ")
#     if number2.isdigit():
#        int_number2 = int(number2)
#        list_numbers.append(int_number2)
#        break
#     else:
#         print("Error, enter correct number!")
# while True:
#     number3 = input("Enter an integer number3: ")
#     if number3.isdigit():
#        int_number3 = int(number3)
#        list_numbers.append(int_number3)
#        break
#     else:
#         print("Error, enter correct number!")
# max_number=max(list_numbers)
# min_number=min(list_numbers)
# median=sum(list_numbers)-max_number-min_number
# print(f"Max number : {max_number}")
# print(f"Min number : {min_number}")
# print(f"Median : {median}")

#TASK-4.
# Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100; якщо число ділиться на 3,
# замість числа виведіть "fizz". Якщо воно ділиться на 5, замість числа виведіть "Buzz".
# Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.
# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("fizz buzz")
#     elif num%3==0:
#         print("fizz")
#     elif num%5==0:
#         print("buzz")
#     else:
#         print(num)

#TASK-5.
# Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100;
# якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM" замість числа.
# for num in range(1,101):
#     if num%7==0 or "7" in str(num):
#         print("BOOM")
#     else:
#         print(num)
