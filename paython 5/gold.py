gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]
prices = [gold_prices_1, gold_prices_2, gold_prices_3, gold_prices_4, gold_prices_5]
for i, x in enumerate(prices, 1):
    max_profit = 0
    day1 = 0
    day2 = 0
    for j in range(len(x)):
        for k in range(j + 1, len(x)):
            profit = x[k] - x[j]
            if profit > max_profit:
                max_profit = profit
                day1 = j + 1
                day2 = k + 1
    print(f"Список {i}:")
    if max_profit > 0:
        print(f"  Купить в день {day1} по {x[day1 - 1]}")
        print(f"  Продать в день {day2} по {x[day2 - 1]}")
        print(f"  Прибыль: {max_profit}")
    else:
        print("  Нет прибыли")
    print()
