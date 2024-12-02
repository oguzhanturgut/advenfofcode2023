from collections import defaultdict

with open("day4.txt", "r") as f:
    lines = f.readlines()
    result = 0
    cards = defaultdict(int)
    for i, line in enumerate(lines):
        cards[i] += 1
        card, vals = [line for line in line.strip().split(": ")]
        wins, nums = vals.split("|")
        wins = [int(win) for win in wins.split()]
        nums = [int(num) for num in nums.split()]
        hit = len(set(wins) & set(nums))
        for j in range(hit):
            cards[i + j + 1] += cards[i]

        result += 2**(hit-1)
    print(result)
    print(sum(cards.values()))
