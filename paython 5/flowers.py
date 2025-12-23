flowers_sets = [ {"rose", "jasmine", "lily"}, {"orchid", "tulip", "violet", "daisy"}, {"lavender", "sunflower"} ]
for flowers_set in flowers_sets:
    scents = 2 ** len(flowers_set)
    print(f"{flowers_set}: {scents} ароматов")