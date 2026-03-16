numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

results = [number for number in numbers if number % 2 == 0]
print(results)

with open ('file1.txt') as file1:
    File_1 = file1.readlines()
    File1 = [int(num.strip()) for num in File_1]

with open ('file2.txt') as file2:
    File_2 = file2.readlines()
    File2 = [int(num.strip()) for num in File_2]

result = [number for number in File1 if number in File2]

print(result)

with open('file1.txt') as file1:
    file_1_data = file1.readlines()

with open('file2.txt') as file2:
    file_2_data = file2.readlines()

results = [int(num) for num in file_1_data if num in file_2_data]

print(results)

# Dictionary Comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {days: ((temperature*9/5) + 32) for (days, temperature) in weather_c.items()}
print(weather_f)
