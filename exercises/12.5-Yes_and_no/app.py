theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def text(num):
    funct_word = ""
    if num == 1:
        funct_word = 'wiki'
    else: 
        funct_word = 'woko'
    return funct_word

new_list = list(map(text,theBools))

print(new_list)
