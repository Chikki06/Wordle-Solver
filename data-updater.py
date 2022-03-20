file = open(r"words.txt","r+")
lines = []
new_words = ""
lines = file.readlines()
for i in lines:
    if len(i) == 6:
            new_words+= (i)
with open(r'updated_word.txt', 'w') as f:
    f.write(new_words)
