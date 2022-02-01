from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    """
        Использование генератора
    """
    # специальный случай
    yield 0
    # специальный случай
    if n > 0:
        yield 1

    # начальное значение fib6(0)
    last_item: int = 0
    # начальное значение fib6(1)
    next_item: int = 1

    for _ in range(1, n):
        last_item, next_item = next_item, last_item + next_item
        yield next_item


if __name__ == "__main__":
    for i in fib6(60):
        print(i)
