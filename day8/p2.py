import math
with open("./input.txt", "r") as inp:
    sequence = inp.readline()[:-1]
    inp.readline()
    dct = {}
    for line in inp:
        arr = line.split()

        dct[arr[0]] = {'L':arr[2][1:-1], 'R':arr[3][:-1]}
    curr = 'AAA'

    def calcstep(start):
        curr = start
        count = 0
        seqnum = 0
        while True:
            step = sequence[seqnum]

            if curr[-1] == 'Z':
                break
            curr = dct[curr][step]
            count += 1
            seqnum += 1
            seqnum = seqnum % len(sequence)

        return count
    
    arr = []
    for x in dct.keys():
        if x[-1] == 'A':
            arr.append(calcstep(x))

    lcmvalue = arr[0]
    for i in arr[1:]:
        lcmvalue = math.lcm(lcmvalue, i)
        
    print(lcmvalue)