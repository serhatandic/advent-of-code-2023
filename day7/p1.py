# categorize each hand
# rank each hand using the categories and relative strength of the letters/numbers
# calculate bid*rank for each hand an sum all
import functools
with open("./input.txt", "r") as inp:
    hand_bid_pairs = {}
    # assign rank to each category to make comparison easier
    typecomp = {
        'five_of_a_kind': 7,
        'four_of_a_kind': 6,
        'full_house': 5,
        'three_of_a_kind': 4,
        'two_pair': 3,
        'one_pair': 2,
        'high_card': 1
    }
    handcomp = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14
    }
    def check_kind(cards):
        dct = {}
        for i in cards:
            if dct.get(i):
                dct[i] += 1
            else:
                dct[i] = 1
        values = list(dct.values())
        if len(set(cards)) == 1:
            return 'five_of_a_kind'
        elif 4 in values:
            return 'four_of_a_kind'
        elif 3 in values and 2 in values:
            return 'full_house'
        elif 3 in values and values.count(1) == 2:
            return 'three_of_a_kind'
        elif 1 in values and values.count(2) == 2:
            return 'two_pair'
        elif 2 in values and values.count(1) == 3:
            return 'one_pair'
        elif values.count(1) == 5:
            return 'high_card'
    
    def compare_hands(hand1, hand2):
        for i in range(0, len(hand1)):
            if handcomp[hand1[i]] == handcomp[hand2[i]]:
                continue
            elif handcomp[hand1[i]] > handcomp[hand2[i]]:
                return 1
            else:
                return -1

    def sorting_key(item):
        key, value = item
        # Use the value for primary sorting
        primary = value
        # Use the custom comparison for secondary sorting when values are equal
        # This creates a unique identifier for each key based on the custom comparison
        secondary = functools.cmp_to_key(lambda x, y: compare_hands(x, y))(key)
        return (primary, secondary)
    
    for line in inp:
        arr = line.split()
        hand_bid_pairs[arr[0]] = int(arr[1])
    
    dct = {}
    for hand in hand_bid_pairs.keys():
        dct[hand] = typecomp[check_kind(hand)]
    
    sorted_dict = sorted(dct.items(), key=sorting_key)

    sum = 0
    for i in range(0, len(sorted_dict)):
        elm,_ = sorted_dict[i]
        sum += hand_bid_pairs[elm] * (i+1)
    print(sum)
    
