# List Comprehension

# numbers = [1, 2, 3]
# new_numbers = [(n + 1) for n in numbers]
# print(new_numbers)
#
# name = "Aline"
# new_list = [letter for letter in name]
# print(new_list)
#
# new_list_range = [(number * 2) for number in range(1, 5)]
# print(new_list_range)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# long_names_upper = [name.upper() for name in names if len(name) > 5]
# print(long_names_upper)

# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.item()}

from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: randint(1, 100) for student in names}
print(students_scores)

passed_student = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_student)
