# 12 red cubes, 13 green cubes, and 14 blue cubes.
stock = {"red": 12, "green":13, "blue":14}

with open("./input.txt", "r") as inp:
    powerList = []
    for gameNumber, line in enumerate(inp, start=1):
        rounds = line[7:].split(';')
        maxRed, maxBlue, maxGreen = 0, 0, 0
        for currRound in rounds:
            blueIndex = currRound.find('blue')
            redIndex = currRound.find('red')
            greenIndex = currRound.find('green')
            blue, red, green = 0, 0, 0

            
            if blueIndex > -1:
                blue = int(currRound[blueIndex - 3:blueIndex].strip())
            if redIndex > -1:
                red = int(currRound[redIndex - 3:redIndex].strip())
            if greenIndex > -1:
                green = int(currRound[greenIndex - 3:greenIndex].strip())
            
            if blue > maxBlue:
                maxBlue = blue
            if red > maxRed:
                maxRed = red
            if green > maxGreen:
                maxGreen = green
            
        
        powerList.append(maxBlue * maxGreen * maxRed)

    print(sum(powerList))


