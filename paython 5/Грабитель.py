items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10
items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10
items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12
items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11
all_cases = [(items_1, time_limit_1, weight_limit_1), (items_2, time_limit_2, weight_limit_2), (items_3, time_limit_3, weight_limit_3), (items_4, time_limit_4, weight_limit_4)]
for num, (a, t, w) in enumerate(all_cases, 1):
    n = len(a)
    best_t = 10**9
    best_cases = []
    for i in range(1 << n):
        ct = 0
        cw = 0
        cv = 0
        cases = []
        for j in range(n):
            if i & (1 << j):
                v, t1, w1 = a[j]
                if cw + w1 <= w:
                    ct += t1
                    cw += w1
                    cv += v
                    cases.append(j)
                else:
                    break
        if cv > 0 and ct < best_t:
            best_t = ct
            best_cases = cases
    print(f" Рюкзак {num}:")
    if best_cases:
        print(f"  Время: {best_t}")
        print(f"  Предметы: {[a[x-1] for x in best_cases]}")
        print(f"  Стоимость: {sum(a[x][0] for x in best_cases)}")
        print(f"  Вес: {sum(a[x][2] for x in best_cases)}")
    else:
        print("  Нельзя взять предметы")
        print()
