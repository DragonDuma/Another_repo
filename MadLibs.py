
print('Hello traveler, I see that you are {irregular verb}. Please rest your {noun} inside here my friend. \
\nThen {verb} on down to the market and {verb} over the haybales.')

# you could also do this:
# '''Hello traveler, I see that you are {irregular verb}. Please rest your {noun} inside here my friend.
# Then {verb} on down to the market and {verb} over the haybales.''' this makes a doc string with maintained
# formatting. Use this to maintain the format because \  or \n are too annoying and keep it as one mega long line,
# you could also make two strings and put \n at the beginning of the second string.
# third method is easiest and that is to use the \ at the end of the line and then \n on the next physical line


irregular_verb = input("Irregular Verb:")
noun = input("Noun:")
verb1 = input("Verb:")
verb2 = input("Verb:")

madlibs_game = f"Hello traveler, I see that you are {irregular_verb}. Please rest your {noun} inside \
\nhere my friend. Then {verb1} on down to the market and {verb2} over the haybales."
# you can also use a \ to continue onto the next line then a \n at the beginning of the continued line
print(madlibs_game)
