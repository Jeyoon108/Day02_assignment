# practice today

# def k(s):
#     def i():
#         return print("a: '%s' " % s)
#     return i
#
# a = k('D')
# print(a)
# a()

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))

for thing in genobj:
    print(thing)

for thing in genobj:
    print(f"{thing}!")

genobj_1 = [pair for pair in zip(['a', 'b'], ['1', '2'])]

print(genobj_1)