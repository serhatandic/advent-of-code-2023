matrix = []
result = []
dct = {}

def isSymbol(ch):
    return not ch.isnumeric() and not (ch == '.')

def checkSurrounding(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 <= (x+i) < len(matrix) and 0 <= (y+j) < len(matrix[x+i]) and isSymbol(matrix[x+i][y+j]):
                return True
    return False

def getWholeNumber(x,y):
    tempy = y + 1
    num = matrix[x][y]
    left, right = x, y
    while tempy < len(matrix[x]) and matrix[x][tempy].isnumeric():
        num += matrix[x][tempy]
        right = tempy
        tempy += 1
    
    tempy = y - 1

    while tempy >= 0 and matrix[x][tempy].isnumeric():
        newnum = matrix[x][tempy] + num
        num = newnum
        tempy -= 1
    
    dct[(left, right)] = int(num)
    return

with open("./input.txt", "r") as inp:
    for line in inp:
        matrix.append(list(line)[:-1])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if (matrix[i][j]).isnumeric() and checkSurrounding(i, j):
            result.append((i,j))

for (i,j) in result:
    getWholeNumber(i,j)

print(sum(dct.values()))