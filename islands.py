
test_isle1 =    [[1,0],
                [0,1]]



test_isle2 =    [[1,0,1,0],
                [0,1,1,0],
                [0,1,0,1]]

def islands(isle):
    islands = 0
    if isle == None or isle == [[]]:
        return islands
    for i in range(len(isle)):
        for j in range(len(isle[0])):
            if isle[i][j] == 1:
                islands += 1
                isle = poison(isle, i, j)
    return islands

def poison(isle,i,j):
    isle[i][j] = 2
    if i+1 in range(0,len(isle)) and isle[i+1][j] == 1:
        poison(isle,i+1,j)
    if i-1 in range(0,len(isle)) and isle[i-1][j] == 1:
        poison(isle,i-1,j)
    if j+1 in range(0,len(isle[0])) and isle[i][j+1] == 1:
        poison(isle,i,j+1)
    if j-1 in range(0,len(isle[0])) and isle[i][j-1] == 1:
        poison(isle,i,j-1)
    return isle

print(islands(test_isle2))
