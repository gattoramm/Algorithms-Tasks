from typing import Dict


# базовые случаи
memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    """
        Использование мемоизации
    """
    if n not in memo:
        # мемоизация
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


if __name__ == "__main__":
    print(fib3(100))
