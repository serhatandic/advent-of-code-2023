
with open("./input.txt", "r") as inp:
    arr = []
    for line in inp:
        splitIndex = line.find(":")
        winning = line.split(":")[1].split('|')[0].strip()
        rest = line.split(":")[1].split('|')[1].strip()
        
        winningNumbers = [int(x) for x in winning.split(" ") if x]
        restNumbers = [int(x) for x in rest.split(" ") if x]
        
        count = 0
        for i in winningNumbers:
            if i in restNumbers:
                count += 1
        
        if count > 0:
            arr.append(2** (count - 1))
    
    print(sum(arr))