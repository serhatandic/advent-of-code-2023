
with open("./input.txt", "r") as inp:
    arr = []
    for num, line in enumerate(inp, 0):
        arr.append([[int(x) for x in line.split()]])

    ind = 0
    for i in range(0, len(arr)):
        while arr[i][-1].count(0) != len(arr[i][-1]):
            arr[i].append([])
            for j in range(0, len(arr[i][ind]) - 1):
                diff = arr[i][ind][j+1] - arr[i][ind][j]
                arr[i][-1].append(diff)
            ind += 1
        ind = 0

    for i in range(0, len(arr) ):
        for j in range(len(arr[i]) - 1, -1, -1):
            if j == len(arr[i]) - 1:
                arr[i][j].append(0)
            else:
                arr[i][j].append(arr[i][j+1][-1] + arr[i][j][-1])
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i][0][-1]

    print(sum)