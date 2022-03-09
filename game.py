valid_words = []

with open('words.txt') as file:
    lines = file.readlines()
for word in lines:
    if len(word) == 6:
        valid_words.append(word)

with open('game.txt', 'a+') as f:
    for word in valid_words:
        f.write(word.lower())
f.close()

print('whats the word you wrote to wordle?')
user_input = input(">")
game_over = False

while not game_over:
    print('which postion of letters(seprated by space) were in the correct spot(enter 0 if none)')
    correct_spots = input(">")
    list_of_correct_spots = correct_spots.split(' ')

    print('which postion of letters(seprated by space) were in the the word(enter 0 if none)')
    correct_spots = input(">")
    list_of_correct_spots = correct_spots.split(' ')

    print('okay lemme think now hmmmmm')
    # work from here
