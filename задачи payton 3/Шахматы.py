def max_rooks(m, n):
    return min(m, n)
def max_knights(m, n):
    return (m * n + 1) // 2
def max_queens(m, n):
    queen_max = {
        (4, 4): 4, (4, 5): 4, (4, 6): 4, (4, 7): 4, (4, 8): 4, (4, 9): 4, (4, 10): 4,
        (5, 5): 5, (5, 6): 5, (5, 7): 5, (5, 8): 5, (5, 9): 5, (5, 10): 5,
        (6, 6): 6, (6, 7): 6, (6, 8): 6, (6, 9): 6, (6, 10): 6,
        (7, 7): 7, (7, 8): 7, (7, 9): 7, (7, 10): 7,
        (8, 8): 8, (8, 9): 8, (8, 10): 8,
        (9, 9): 9, (9, 10): 9, (10, 10): 10}
    return queen_max.get((m, n), min(m, n))
def max_kings(m, n):
    return ((m + 1) // 2) * ((n + 1) // 2)
def max_chesspieces(problem_count, problems):
    results = []
    for piece, m, n in problems:
        if piece == 'r':  # Ладья
            results.append(max_rooks(m, n))
        elif piece == 'k':  # Конь
            results.append(max_knights(m, n))
        elif piece == 'Q':  # Ферзь
            results.append(max_queens(m, n))
        elif piece == 'K':  # Король
            results.append(max_kings(m, n))
    return results
def main():
    # Ввод данных
    problem_count = int(input("Количество задач: "))
    problems = []
    for i in range(problem_count):
        data = input(f"Задача {i + 1} : ").split()
        piece = data[0]
        m = int(data[1])
        n = int(data[2])
        problems.append((piece, m, n))
    results = max_chesspieces(problem_count, problems)
    print("\nРезультаты:")
    for result in results:
        print(result)
if __name__ == "__main__":
    main()