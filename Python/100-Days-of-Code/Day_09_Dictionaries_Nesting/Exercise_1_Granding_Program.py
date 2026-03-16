student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name in student_scores:
    value = student_scores[name]
    if((value <= 70)):
        grade = "Fail"
    elif((value >= 71) and (value <= 80)):
        grade = "Acceptable"
    elif((value >= 81) and (value <= 90)):
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[name] = grade

print(student_grades)