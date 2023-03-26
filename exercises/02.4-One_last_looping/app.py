names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
len_names = len(names)
names[0] = (names[2]+names[4])
names[1] = "Steven"
names[-1] = "Pepe"
        


for r in range(len_names-1, -1, -1):
    print(names[r])
