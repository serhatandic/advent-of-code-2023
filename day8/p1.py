with open("./input.txt", "r") as inp:
    sequence = inp.readline()[:-1]
    inp.readline()
    dct = {}
    for line in inp:
        arr = line.split()

        dct[arr[0]] = {'L':arr[2][1:-1], 'R':arr[3][:-1]}
    
    count = 0
    curr = 'AAA'
    seqnum = 0
    while True:
        step = sequence[seqnum]
        if curr == 'ZZZ':
            break
        curr = dct[curr][step]
        count += 1
        seqnum += 1
        seqnum = seqnum % len(sequence)

    print(count)