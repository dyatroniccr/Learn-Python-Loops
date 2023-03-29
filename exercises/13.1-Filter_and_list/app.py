
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def names_w_r(name):
    return name[0] == 'R'
        

resulting_names = list(filter(names_w_r, all_names))
print(resulting_names)




