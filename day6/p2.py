with open("./input.txt", "r") as inp:
    times = []
    distances = []

    line = inp.readline()
    seperator_index = line.find(':')
    times = line[seperator_index + 1:].split()

    line = inp.readline()
    seperator_index = line.find(':')
    distances = line[seperator_index + 1:].split()

    time, distance = "", ""

    for tmp in times:
        time += tmp
    
    for tmp in distances:
        distance += tmp


    time, distance = int(time), int(distance)
    results = []
    step = 1
    hold = 1
    while hold < time:
        print(hold / time)
        speed = hold
        maxreachable = speed * (time - hold)
        if maxreachable > distance:
            results.append(hold)
                    
    print(max(results) + 1 - min(results))
