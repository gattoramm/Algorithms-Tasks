from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    """
        Использование автомемоизации с декоратором
    """
    # базовый случай
    if n < 2:
        return n
    # рекурсивный случай
    return fib4(n - 1) + fib4(n - 2)


if __name__ == "__main__":
    print(fib4(40))
