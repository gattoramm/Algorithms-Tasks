def fib2(n: int) -> int:
    """
        общее определение с учетом базовых случаев
    """
    if n < 2:
        # базовый случай
        return 1
    # рекурсивный случай
    return fib2(n - 1) + fib2(n - 2)


if __name__ == "__main__":
    print(fib2(40))
