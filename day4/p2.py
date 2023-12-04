
with open("./input.txt", "r") as inp:
    arr = [] # stack
    lineNumber = 1
    for line in inp:
        splitIndex = line.find(":")
        winning = line.split(":")[1].split('|')[0].strip()
        rest = line.split(":")[1].split('|')[1].strip()
        
        winningNumbers = [int(x) for x in winning.split(" ") if x]
        restNumbers = [int(x) for x in rest.split(" ") if x]
        
        arr.append((winningNumbers, restNumbers, lineNumber))
        lineNumber += 1

    arrCopy = arr.copy()

    for card in arr:
        winningNumbers = card[0]
        restNumbers = card[1]
        cardNumber = card[2]

        count = 0
        for i in winningNumbers:
            if i in restNumbers:
                count += 1

        for i in range(1, count+1):
            arr.append((arrCopy[cardNumber - 1 + i][0], arrCopy[cardNumber - 1 + i][1], cardNumber + i))
    
    print(len(arr))