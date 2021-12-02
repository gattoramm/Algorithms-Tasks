"""
    использование генератора
"""


from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0     # специальный случай
    if n > 0: yield 1       # специальный случай

    last: int = 0   # начальное значение fib6(0)
    next: int = 1   # начальное значение fib6(1)

    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == "__main__":
    for i in fib6(60):
        print(i)
