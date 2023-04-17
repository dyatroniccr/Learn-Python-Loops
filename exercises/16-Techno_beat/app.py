

# Your code go above, nothing to change after this line:

def lyrics_generator(listGen):
    especial_lyrics = 0
    lyrics = ""
    for x in listGen:
        if x == 1:
            lyrics += "Drop the base "
            especial_lyrics += 1
            if especial_lyrics == 3:
                lyrics += "!!!Break the base!!! "
                especial_lyrics = 0
        else:
            lyrics += "Boom "

    return lyrics
            

print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))