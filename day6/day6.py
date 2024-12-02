import math
from functools import reduce

with open("day6.txt", "r") as f:
    lines = f.readlines()
    times = [i for i in lines[0].split(":")[1].strip().split()]
    time = reduce(lambda x, y: x + y, times)
    time = int(time)
    distances = [i for i in lines[1].split(":")[1].strip().split()]
    distance = reduce(lambda x, y: x + y, distances)
    distance = int(distance)


    # print(times, distances)
    # beats = []
    # for i, time in enumerate(times):
    # beat = 0
    # time = int(time)
    hit = 0
    for j in range(time + 1):
        dist = j * (time - j)
        if dist >= distance:
            # print(dist, distance)
            # print(j)
            hit += 1
            # break
            # beat += 1
    # print(beat)
    # beats.append(beat)
    # print(math.prod(beats))
    # print(time - (2 * hit))
    print(hit)
