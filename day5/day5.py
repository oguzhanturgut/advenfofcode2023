def convert(seed, rest):
    for line in rest:
        dest, source, range = [int(seed) for seed in line.split()]
        if source <= seed <= source + range:
            return dest + (seed - source)
    return seed


with open("day5.txt", "r") as f:
    lines = f.read().strip()
    parts = lines.split("\n\n")
    seeds, *rest = parts
    seeds = seeds.split(":")[1].split()
    print(seeds)
    res = []
    for seed in seeds:
        seed = int(seed)
        for r in rest:
            seed = convert(seed, r.split("\n")[1:])
        res.append(seed)
    print(min(res))
