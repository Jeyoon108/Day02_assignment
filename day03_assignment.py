# Chap 6 #3

guess_me = int(input("Input any number : ")) #5

for number in range(10):
    if number < guess_me:
        print(f"It's not {number}, still too low")
    else:
        print(f"found it! Input number was {guess_me}")
        break

