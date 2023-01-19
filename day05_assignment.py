# Chap9 # 1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
#
#
# print(good())

# Chap9 # 2

count = 0
def get_odds():
    for num in range(10):
        if num % 2:
            yield num


odds = get_odds()

for odd in odds:
    count += 1
    if count == 3:
        print(odd)

for odd in odds:  # generator이므로 아무것도 반환하지 않음
    count += 1
    if count == 3:
        print(odd)