def get_resistor_value(x):
    a = {'bk': 0, 'br': 1, 'rd': 2, 'or': 3, 'yl': 4,
    'gr': 5, 'bl': 6, 'vi': 7, 'gy': 8, 'wh': 9}
    b = {'bk': 1, 'br': 10, 'rd': 100, 'or': 100, 'yl': 10000,
    'gr': 100000, 'bl': 1000000, 'vi': 10000000, 'gy': 100000000, 'wh': 1000000000}
    c = {'br': 1, 'rd': 2, 'yl': 5, 'gr': 0.5, 'bl': 0.25, 'vi': 0.1,
    'gy': 0.05, 'au': 5, 'ag': 10, '-': 20}
    if len(x) < 4:
        print(x)
        return None, None
    if any(i not in a for i in x[:3]) or x[3] not in c:
        print(x)
        return None, None
    m1 = a[x[0]]
    m2 = a[x[1]]
    m3 = b[x[2]]
    m4 = c[x[3]]
    y = (m1 * 10 + m2) * m3
    return y, m4
print(get_resistor_value(['br', 'bk', 'yl', 'ag']))
