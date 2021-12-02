"""
    использование автомемоизации с декоратором
"""


from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:   # базовый случай
        return n

    return fib4(n - 1) + fib4(n - 2)     # рекурсивный случай

if __name__ == "__main__":
    print(fib4(40))
