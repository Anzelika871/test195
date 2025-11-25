def mutual_cycle(n):
    dictionary = {}
    r = 1
    position = 0
    while r != 0:
        r = (r * 10) % n
        if r in dictionary:
            return position - dictionary[r]
        dictionary[r] = position
        position += 1
    return 0
print("Введите максимальное d:")
n = int(input())
begin_d = 0
max_len = 0
for d in range(2, n):
    length = mutual_cycle(d)
    if length > max_len:
        max_len = length
        begin_d = d
print(f"d = {begin_d}, длина цикла = {max_len}")