#Import random

#Create the function below:
def matrixBuilder(number):
    colums = []
    for x in range(number):
        row = []         
        for y in range(number):
            row.append(1)

        colums.append(row)        
    
    return colums

print(matrixBuilder(5))