with open("./input.txt", "r") as inp:
    numdict = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    arr = []
    for line in inp:
        num = []
        occurence = 9999
        place = 9999
        k = ""
        for i in range(0, len(line)):
            if line[i].isnumeric():
                occurence = min(occurence,i)
            for key in numdict.keys():
                q = line.find(key) 
                if q != -1 and q < place:
                    k = key
                    place = q
        if place < occurence:
            num.append(numdict[k])
        else:
            num.append(line[occurence])
        occurence = -1
        place = -1
        k = ""
        for i in range(0, len(line)):
            if line[i].isnumeric():
                occurence = max(occurence,i)
            for key in numdict.keys():
                q = line.rfind(key)
                if q > place:
                    k = key
                    place = q

        if place > occurence:
            num.append(numdict[k])
        else:
            num.append(line[occurence])

        numstr = num[0] + num[1]
        print(num, numstr)
        arr.append(int(numstr))
    
    print(sum(arr))