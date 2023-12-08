# seed = source
# soil = destination
# xx (dest) xx (source) xx (length)
from threading import Thread, Lock

def split_into_pairs(lst):
    return [lst[i:i + 2] for i in range(0, len(lst), 2)]

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

pairseeds = split_into_pairs(seeds)
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
locs = set()
lock = Lock()
lock2 = Lock()
def divide_range_into_pieces(fst, snd, pieces=8):
    total_range = snd - fst
    piece_size, remainder = divmod(total_range, pieces)

    ranges = []
    start = fst

    for i in range(pieces):
        end = start + piece_size + (1 if i < remainder else 0)
        ranges.append((start, end))
        start = end

    return ranges

def calculate_location_splitted(pair):
    minval = float('inf')
    for i in range(pair[0], pair[1]):
        newnum = i
        for dct in dctlist:
            for (elm,step) in dct.keys():
                if newnum >= elm and elm + step > newnum:
                    diff = newnum - elm
                    (num, _) = dct.get((elm,step))
                    newnum = num + diff
                    break
            minval = min(minval, newnum)
    with lock:
        locs.add(minval)

def calculate_location(pair):
    ranges = divide_range_into_pieces(pair[0], pair[0] + pair[1], 100000)
    threads = []
    start = 0
    end = 2000
    while end < 100000:
        print(start / 100000)
        for i in ranges[start:end]:
            threads.append(Thread(target=calculate_location_splitted, args=(i,)))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        threads = []
        start = end
        end += 2000
    print(min(locs))
    
for i in range(9, -1, -1):
    pair = pairseeds[i]
    calculate_location(pair)


print(min(locs))