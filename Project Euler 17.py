#1. Way
import inflect

p = inflect.engine()

top = 0
for i in range(1, 1001):
    num = p.number_to_words(i).replace(" ", "").replace("-", "")
    for j in num:
        top += 1
print(top)

# 2. Way
nums = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8,
}

top = 0

for i in range(1, 21):
    top += nums[i]

for i in range(21, 100):
    top += nums[(i // 10) * 10] + nums[i % 10]

for i in range(100, 1000):
    hundreds = i // 100
    tens_and_ones = i % 100

    top += nums[hundreds] + nums[100]
    if tens_and_ones != 0:
        top += 3
        if tens_and_ones <= 20:
            top += nums[tens_and_ones]
        else:
            top += nums[(tens_and_ones // 10) * 10] + nums[tens_and_ones % 10]
top += nums[1] + nums[1000]
print(top)