row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

digit1 = int(position[0])
digit2 = int(position[1])

map[digit2 - 1][digit1 - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

