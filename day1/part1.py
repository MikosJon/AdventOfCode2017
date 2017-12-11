# run the file as python part1.py < input.txt
number = input()
count = 0
for index in range(0, -len(number), -1):
    if number[index] == number[index-1]:
        count += int(number[index])

print(count)
