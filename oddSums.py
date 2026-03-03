# Auther SnehalNakhawa
# Date 10th February 2026
# Description - Calculate odd number between two random values

import random

num1 = random.randint(1, 10)
num2 = random.randint(11, 20)

total = 0
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        total += i
print(f"The first random number was {num1}, the second random number was {num2} and the sum is {total}.")
