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

    print(maps)
    # print(maps['AAA'])
    # print(type(maps['AAA']))
    # print(maps['AAA'][int(directions[0])])
    # print(directions)

    start = 'AAA'
    end = ''
    dir_index = 0
    counter = 0
    while end != 'ZZZ':
        counter += 1
        end = maps[start][int(directions[dir_index])]
        start = end
        if len(directions) == dir_index + 1:
            dir_index = -1
        dir_index += 1

    print(counter)