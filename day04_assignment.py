# Chap7 # 1

i = int(input("출생년도를 입력하세요 : "))
year_list = []
for k in range(0, 5+1):
    year_list = year_list + [i+k]

print(year_list)