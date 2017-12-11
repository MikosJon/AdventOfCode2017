# run the file as python part2.py < input.txt
number = input()
count = 0

step = len(number) // 2

for index in range(len(number)):
    if number[index] == number[(index+step)%len(number)]:
        count += int(number[index])

print(count)
