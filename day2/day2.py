from collections import defaultdict

with open("day2.txt", "r") as file:
    res = 0
    games = []
    limit = {"red": 12, "green": 13, "blue": 14}
    for i, line in enumerate(file):
        colors = defaultdict(int)
        ok = True
        game_id, rounds = line.strip().split(": ")
        game_id = game_id.split(" ")[1]
        rounds = [[r for r in rnd.split(", ")] for rnd in rounds.split("; ")]
        print(game_id, rounds)

        for j, rnd in enumerate(rounds):
            for k, dice in enumerate(rnd):
                cnt, color = dice.split()
                colors[color] = max(colors[color], int(cnt))
                print(color, colors[color])
                if int(cnt) > limit[color]:
                    ok = False
                    # print(f"Game {game_id} is invalid")
        result = 1
        print(colors.values())
        for c in colors.values():
            result *= c
            print(result)
        # if ok:
            # games.append(game_id)
            # res += int(game_id)
        res += result
    print(res)
