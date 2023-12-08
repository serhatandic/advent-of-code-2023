# seed = source
# soil = destination
# xx (dest) xx (source) xx (length)
from threading import Thread

def calculate_single_mapping(mapping, dct):
    with open(f"./{mapping}.txt", "r") as inp:
        for rawline in inp:
            line = rawline[:-1]

            arr = [int(x) for x in line.split()]
            dest, source = arr[0], arr[1]
            dct[(source, arr[2])] = (dest, arr[2])
            
seeds = []
with open("./input.txt", "r") as inp:
    seeds = [int(x) for x in inp.readline()[7:].split()]

allmappings = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

ssdct = {}
sfdct = {}
fwdct = {}
wldct = {}
ltdct = {}
thdct = {}
hldct = {}

dctlist = [ssdct, sfdct, fwdct, wldct, ltdct, thdct, hldct]
threads = []
for i in range(0, len(allmappings)):
    threads.append(Thread(target=calculate_single_mapping, args=(allmappings[i], dctlist[i])))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
locs = []
for i in seeds:
    newnum = i
    for dct in dctlist:
        for (elm,step) in dct.keys():
            if newnum >= elm and elm + step > newnum:
                diff = newnum - elm
                (num, _) = dct.get((elm,step))
                newnum = num + diff
                break

    locs.append(newnum)

print(min(locs))