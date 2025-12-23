items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5
items_2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
weight_limit_2 = 10
items_3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
weight_limit_3 = 7
items_4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
weight_limit_4 = 7
items_5 = [(6, 10), (8, 15), (12, 30)]
weight_limit_5 = 5
backpack = [(items_1, weight_limit_1), (items_2, weight_limit_2), (items_3, weight_limit_3), (items_4, weight_limit_4), (items_5, weight_limit_5)]
for i, (a, l) in enumerate(backpack, 1):
    n = len(a)
    best = 0
    best_items = []
    for x in range(1 << n):
        w = 0
        v = 0
        items_now = []
        for y in range(n):
            if x & (1 << y):
                w1, v1 = a[y]
                if w + w1 <= l:
                    w += w1
                    v += v1
                    items_now.append(y)
                else:
                    break
        if v > best:
            best = v
            best_items = items_now
    if best > 0:
        print(f"Рюкзак {i}:")
        print(f"  Стоимость: {best}")
        print(f"  Предметы: {[a[b] for b in best_items]}")
        print()
    else:
        print(f"Рюкзак {i}: ")
        print("   Нет места")