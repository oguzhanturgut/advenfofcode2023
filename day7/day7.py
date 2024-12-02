import functools
from collections import defaultdict
from enum import Enum

cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6,
         '5': 5, '4': 4, '3': 3, '2': 2}

class Type(Enum):
    (FiveOfAKind, FourOfAKind, FullHouse, ThreeOfAKind, TwoPair, OnePair,
     HighCard) = range(7, 0, -1)


def compare(x, y):
    hand1 = list(x[0])
    hand2 = list(y[0])
    for i in range(5):
        if cards[hand1[i]] > cards[hand2[i]]:
            return 1
        elif cards[hand1[i]] < cards[hand2[i]]:
            return -1
    return 0

def match_hand(hand):
    set_val = set(list(hand))
    if len(set_val) == 1:
        return Type.FiveOfAKind
    if len(set_val) == 2:
        if hand.count(set_val.pop()) == 4 or hand.count(set_val.pop()) == 4:
            return Type.FourOfAKind
        else:
            return Type.FullHouse
    if len(set_val) == 3:
        if hand.count(set_val.pop()) == 3 or hand.count(
                set_val.pop()) == 3 or hand.count(set_val.pop()) == 3:
            return Type.ThreeOfAKind
        else:
            return Type.TwoPair
    if len(set_val) == 4:
        return Type.OnePair
    if len(set_val) == len(hand):
        return Type.HighCard


with open("day7.txt") as f:
    lines = f.readlines()
    hands = defaultdict()
    for line in lines:
        hand, bid = line.split()
        hands[hand] = int(bid)
        # print(hand, match_hand(hand))

    result = ([(hand,match_hand(hand).value,bid) for hand, bid in hands.items()])
    print(sorted(result, key=lambda x: (x[1], functools.cmp_to_key(compare)), reverse=True))
    # print(sorted(result, key=functools.cmp_to_key(compare), reverse=True))




    # print(sorted(hands.items(), key=lambda x: x[1]))
    # print(sorted(hands.keys(), key=functools.cmp_to_key(compare), reverse=True))
    # print(set(list(list(hands.keys())[0])))
