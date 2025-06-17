# TASK
# У класі професора Грубла щойно був іспит. Він почав перевіряти роботи, але
# оцінював їх не дуже уважно.
# Напишіть програму, яка  приймає як вхідні дані оцінку кожного учня і те, чи здав він
# іспит.
# Потім програмі необхідно надрукувати дві речі:
# 1). Чи був професор Грубл послідовним у проставленні позначки
# "Passed" для студентів.
# 2). Якщо професор Грубл був послідовним, виведіть діапазон у
# якому знаходиться поріг для складання іспиту.

def check_correct_assessment():
    while True:
        number = input("Введіть кількість студентів, які брали  участь в іспиті: ")
        if number.isdigit():
            number_students = int(number)
            break
        else:
            print("Помилка! Введіть коректне число!")
    import random
    students_scores=[]
    for i in range(1,number_students+1):
        score_student=[random.randint(50,100), random.choice([True, False])]
        students_scores.append(score_student)
    print(students_scores)
    passing_scores=[score for score, result in students_scores if result]
    # print(passing_scores)
    failing_scores=[score for score, result in students_scores if not result]
    # print(failing_scores)
    min_passing_score=min(passing_scores,default=100) #min прохідний бал
    # print(min_passing_score)
    max_failing_score=max(failing_scores,default=50)# max непрохідний бал
    # print(max_failing_score)
    if min_passing_score<=max_failing_score:
        return "Професор Грубл НЕ послідовний в оцінюванні "
    else:
        return (f"Професор Грубл є послідовний, поріг складання іспиту знаходиться в межах {max_failing_score+1}-{min_passing_score} балів")

print(check_correct_assessment())

# Вітаю! Спробувала вирішити це завдання, використовуючи словник. Але бачу, що після створення
# словника, я ніде більше не використовую ключ (id-студента). То чи раціональний цей спосіб?
# Чи по-іншому потрібно було розв'язувати через словник? Не можу зрозуміти, підкажіть,
# будь ласка, де я помиляюся?
# Дякую!


# # 2 спосіб,  використовуючи словник
#
# def check_correct_assessment2(number_of_students):
#  # 1) ФОРМУВАННЯ СЛОВНИКА
#     students_id=[]
#     student_score_all = []
#     for number in range(1,number_of_students+1):
#         list_student_score=[]
#
#         while True:
#             id_student = input("Введіть унікальний номер студента: ")
#             if id_student not in students_id:
#                 students_id.append(id_student)
#                 break
#             else:
#                 print("Помилка! Tакий id студента вже вводили")
#
#         while True:
#             score = input("Введіть кількість балів, яку отримав студент: ")
#             if score.isdigit() and 50<=int(score)<=100:
#                 score_student = int(score)
#                 break
#             else:
#                 print("Помилка! Введіть коректне число!")
#
#         while True:
#             result = input("Введіть вердикт P (passed) або F (failed) ")
#             if result=='P' or result=='F':
#                 result_student = result
#                 break
#             else:
#                 print("Помилка! Введіть коректне значення вердикту:!")
#         list_student_score.append(score_student)
#         list_student_score.append(result)
#         student_score_all.append(list_student_score)
#         dict_students_result=dict(zip(students_id, student_score_all))
#     print(student_score_all)
#     print(f"Сформований словник результатів іспиту: {dict_students_result}")
#
#  # 2) ОБРОБКА СЛОВНИКА (ОТРИМАНИХ РЕЗУЛЬТАТІВ)
#     student_scores=[]
#     for value in dict_students_result.values():
#         student_scores.append(value)
#     print(student_scores)
#     passing_scores = [score for score, result in student_scores if result=='P']
#     print(passing_scores)
#     failing_scores=[score for score, result in student_scores if result=='F']
#     print(failing_scores)
#     min_passing_score=min(passing_scores,default=100) #min прохідний бал
#     print(min_passing_score)
#     max_failing_score=max(failing_scores,default=50)# max непрохідний бал
#     print(max_failing_score)
#     if min_passing_score<=max_failing_score:
#         return "Професор Грубл НЕ послідовний в оцінюванні "
#     else:
#         return (f"Професор Грубл є послідовний, поріг складання іспиту знаходиться в межах {max_failing_score+1}-{min_passing_score} балів")
#
# print(check_correct_assessment2(3))