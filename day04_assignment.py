# Chap8 #1 ~ #5

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}  # #1

print(e2f['walrus'])  # #2

e2f_list = list(e2f.items())
f2e = {}
for k, v in e2f_list:
    f2e = {**f2e, **{v: k}}
print(f2e)  # #3

print(f2e['chien'])  # #4

print(list(e2f.keys()))  # #5
