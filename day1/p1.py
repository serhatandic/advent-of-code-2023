with open("./input.txt", "r") as inp:
    arr = []
    for line in inp:
        num = ""
        for letter in line:
            if letter.isnumeric():
                num += letter
                break
        for letter in line[::-1]:
            if letter.isnumeric():
                num += letter
                break
        if num:
            arr.append(int(num))
    
    print(sum(arr))