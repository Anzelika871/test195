import math
def complexity_table(sizes):
    print("n      O(1)  O(log n)  O(sqrt(n))  O(n)  O(n log n)  O(n^2)    O(n^3)    O(2^n)      O(n!)")
    print("-" * 90)
    for n in sizes:
        o1 = 1
        o_log_n = round(math.log2(n) if n > 0 else 0, 2)
        o_sqrt_n = round(math.sqrt(n), 2)
        o_n = n
        o_n_log_n = round(n * math.log2(n) if n > 0 else 0, 2)
        o_n2 = n ** 2
        o_n3 = n ** 3
        o_2n = 2 ** n
        if n <= 10:
            o_n_fact = math.factorial(n)
        else:
            o_n_fact = "очень большое"
        print(
            f"{n:<6} {o1:<6} {o_log_n:<9} {o_sqrt_n:<11} {o_n:<6} {o_n_log_n:<11} {o_n2:<9} {o_n3:<9} {o_2n:<11} {o_n_fact}")
def main():
    input_str = input("Введите размеры данных через пробел: ")
    sizes = [int(x) for x in input_str.split()]
    complexity_table(sizes)
if __name__ == "__main__":
    main()