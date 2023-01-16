# Chap4 연습문제 #1
# import random
#
# secret = random.randint(1, 10)
# guess = int(input('정답은 ?'))
#
# if secret == guess:
#     print("정답 입니다!")
# elif guess > secret:
#     print(f"정답보다 큰 수 입니다. 정답은{secret}")
# else:
#     print(f"정답보다 작은 수 입니다. 정답은{secret}")

# Chap4 연습문제 #2
import random

small = random.randint(0, 1)
green = random.choice([True, False])

print(small)
print(green)

if small:
    if green:
        print("It's a pea")
    else:
        print("It's a cherry")
else:
    if green:
        print("It's a watermelon")
    else:
        print("It's a pumpkin")