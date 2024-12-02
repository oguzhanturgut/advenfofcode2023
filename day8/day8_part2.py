with open('day8.txt') as f:
    lines = f.readlines()
    directions = lines[0]
    directions = directions.strip().replace('L', '0').replace('R', '1')

    mapping = lines[2:]
    mapping = [line.strip().split(' = ') for line in mapping]
    maps = {}
    for map in mapping:
        map1 = map[1].replace('(', '').replace(')', '').split(', ')
        maps[map[0]] = map1

    ends_with_A = list(filter(lambda x: x[2] == 'A', maps.keys()))

    counter = 0
    while all([x[2] == 'Z' for x in ends_with_A]) is False:
        print(ends_with_A, counter)
        dir_index = 0
        counter += 1
        # starts_with_A = []
        for i, start in enumerate(ends_with_A):
            ends_with_A[i] = maps[start][int(directions[dir_index])]
        if len(directions) == dir_index + 1:
            dir_index = -1
        dir_index += 1

    print(counter)

