def fib5(n: int) -> int:
    """
        Использование итеративного метода
    """
    # специальный случай
    if n == 0:
        return n
    # начальное значение fib5(0)
    last_item: int = 0
    # начальное значение fib5(1)
    next_item: int = 1

    for _ in range(n):
        last_item, next_item = next_item, last_item + next_item
    return next_item


if __name__ == "__main__":
    print(fib5(60))
