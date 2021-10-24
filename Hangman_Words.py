import sys
words = 'I used splitlines on the list and then assigned the proper listing to a new variable'

# print(words.splitlines())  # splitlines can only be used on a string and in this case you cannot paste a vertical list
# of words like I did above because a string cannot extend to multiple lines without the \ character for each line
# this is really a consequence of the separate line for each word. I converted to a docstring then used splitlines to
# make it a list
# splitlines() is dangerous use it sparingly to convert multiple lines of single word docstrings to lists of comma
# separated strings.
# The logic of it can mess up especially with short strings
# it only separates on each new physical newline and each \n newline

words_in_a_list = ['sausage', 'blubber', 'pencil', 'cloud', 'moon', 'water', 'computer', 'school', 'network', 'hammer',
                   'walking', 'violently', 'mediocre', 'literature', 'chair', 'two', 'window', 'cords', 'musical',
                   'zebra', 'xylophone', 'penguin', 'home', 'dog', 'final', 'ink', 'teacher', 'fun', 'website', 'banana',
                   'uncle', 'softly', 'mega', 'ten', 'awesome', 'attach', 'blue', 'internet', 'bottle', 'tight', 'zone',
                   'tomato', 'prison', 'hydro', 'cleaning', 'television', 'send', 'frog', 'cup', 'book', 'zooming',
                   'evily', 'gamer', 'lid', 'juice', 'moniter', 'Goku', 'Vegeta', 'Freiza', 'Stardust', 'Killer',
                   'captain', 'bonding', 'loudly', 'thudding', 'guitar', 'shaving', 'hair', 'soccer', 'water', 'racket',
                   'table', 'late', 'media', 'desktop', 'flipper', 'club', 'flying', 'smooth', 'monster', 'purple',
                   'guardian', 'bold', 'hyperlink', 'presentation', 'world', 'national  ', 'comment', 'element',
                   'magic', 'lion', 'sand', 'crust', 'toast', 'jam', 'hunter', 'forest', 'foraging', 'silently',
                   'tawesomated', 'joshing', 'pong']
print(sys.getsizeof(words_in_a_list))
