"""
    общее определение с учетом базовых случаев
"""


def fib2(n: int) -> int:
    if n < 2:
        return 1    # базовый случай
    return fib2(n - 1) + fib2(n - 2)    # рекурсивный случай

if __name__ == "__main__":
    print(fib2(40))
