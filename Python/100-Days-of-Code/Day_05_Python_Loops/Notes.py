"""For Loop"""
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

"""For Loop with Range"""
# for number in range(1, 11, 3):
#   print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)