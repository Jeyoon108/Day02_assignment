# Chap7 #11

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

# start 1 각 문자열 출력 후 rhymes의 첫 번째 출력 (첫 글자 대문자, 형태: 단어! 단어! 단어! 첫번째!)
# start 2와 공백 출력 후 rhymes의 문자열과 마침표 출력

first_start1 = []
for song in rhymes:
    for rap in start1:
        print(rap.capitalize(), end='! ')
    print(f'{song[0].capitalize()}!')
    print(f'{start2} {song[1]}.')

