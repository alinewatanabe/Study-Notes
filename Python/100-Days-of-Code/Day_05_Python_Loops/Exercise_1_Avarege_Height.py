student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

i = 0
for c in student_heights:
    i += 1

s = 0
for a in student_heights:
    s += a

average = round(s/i)

print(average)