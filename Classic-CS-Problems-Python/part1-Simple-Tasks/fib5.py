"""
    использование итеративного метода
"""


def fib5(n: int) -> int:
    if n == 0:   # специальный случай
        return n

    last: int = 0   # начальное значение fib5(0)
    next: int = 1   # начальное значение fib5(1)

    for _ in range(n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib5(60))
