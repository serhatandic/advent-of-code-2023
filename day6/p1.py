with open("./input.txt", "r") as inp:
    times = []
    distances = []

    line = inp.readline()
    seperator_index = line.find(':')
    times = [int(x) for x in line[seperator_index + 1:].split()]

    line = inp.readline()
    seperator_index = line.find(':')
    distances = [int(x) for x in line[seperator_index + 1:].split()]

    results = []

    for i in range(0, 4):
        results.append([])
        for hold in range(1, times[i]):
            speed = hold
            maxreachable = speed * (times[i] - hold)
            if maxreachable > distances[i]:
                results[i].append(hold)
                
    res = 1
    print(results)
    for i in results:
        res *= len(i)
        print(len(i))

    print(res)