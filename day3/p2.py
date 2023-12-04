matrix = []
result = []
dct = {}
multDct = {}

def isSymbol(ch):
    return not ch.isnumeric() and not (ch == '.')
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
    return num
def checkSurrounding(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 <= (x+i) < len(matrix) and 0 <= (y+j) < len(matrix[x+i]) and isSymbol(matrix[x+i][y+j]):
                if matrix[x+i][y+j] == '*':
                    if multDct.get((x+i,y+j)):
                        multDct[(x+i,y+j)].add(getWholeNumber(x,y))
                    else:
                        multDct[(x+i,y+j)] = set()
                        multDct[(x+i,y+j)].add(getWholeNumber(x,y))
                return True
    return False



with open("./input.txt", "r") as inp:
    for line in inp:
        matrix.append(list(line)[:-1])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if (matrix[i][j]).isnumeric() and checkSurrounding(i, j):
            result.append((i,j))

for (i,j) in result:
    getWholeNumber(i,j)

sum = 0

for x in multDct.values():
    if len(x) == 2:
        temp = []
        for item in x:
            temp.append(int(item))
        sum += temp[0] * temp[1]
        temp = []

print(sum)