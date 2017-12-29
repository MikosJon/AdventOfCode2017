num_prime = 0
for num in range(106500, 123501, 17):
    for pos_divider in range(2, int(num**0.5)+1):
        if num % pos_divider == 0:
            break
    else:
        num_prime += 1

print(1001 - num_prime) # 1001 is c - b + 1
