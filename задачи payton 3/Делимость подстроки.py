def solution():
    numbers = [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
    total = sum(numbers)
    print(f"\nСумма всех таких чисел: {total}")
    num_str = str(numbers[0])
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        substring = num_str[i + 1:i + 4]
        result = int(substring) % primes[i]
if __name__ == "__main__":
    solution()