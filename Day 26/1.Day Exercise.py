# List Comprehension


# # Using for loop #
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)


# # Using list comprehension #
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Rajdip"
# new_list = [letter for letter in name]
# print(new_list)

# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)
 
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# sort_names = [name for name in names if (len(name) < 5)]
# long_names = [name.upper() for name in names if (len(name) >= 5)]
# print(long_names)


# Dictionary Comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


