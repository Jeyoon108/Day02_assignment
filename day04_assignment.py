# Chap8 #13

keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

zip_dict = dict(zip(keys,values))

print(zip_dict)

# Chap8 #14

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movie = {title: plot for title, plot in zip(titles, plots)}
print(movie)