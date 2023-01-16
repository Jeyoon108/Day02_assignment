# Chap 6 #2

guess_me = int(input("Input any number : ")) #7
number = int(input("Input lower number : ")) #1

while number <= guess_me:
    if number < guess_me:
        print(f"It's not {number}, still too low")
        number += 1
    else:
        print(f"found it! Input number was {guess_me}")
        break
else:
    print('oops,,')