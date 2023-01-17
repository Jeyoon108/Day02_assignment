# Chap7 #8 ~ #9

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()
surprise_list = list(surprise[2])
surprise_list.reverse()
# surprise_list = list(surprise_list)
surprise_list = ''.join(surprise_list)
surprise_list = surprise_list.capitalize()
surprise[2] = surprise_list

print(surprise_list)
print(surprise)
