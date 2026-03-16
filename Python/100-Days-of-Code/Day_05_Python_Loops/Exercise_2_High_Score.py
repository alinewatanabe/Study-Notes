student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

c = 0
highest_score = 0
for c in student_scores:
    if(c > highest_score):
        highest_score = c

print(f"The highest score in the class is: {highest_score}")
