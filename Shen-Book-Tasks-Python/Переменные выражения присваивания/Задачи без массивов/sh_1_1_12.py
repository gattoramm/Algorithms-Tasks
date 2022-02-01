def sh_1_1_12(n: int) -> float:
    """
        Вычисление 1/0! + 1/1! +...+ 1/n! с количеством оперций порядка n
    """
    result = mp = 1.0

    for k in range(1, n + 1):
        mp *= k
        result += 1 / mp
    return result


if __name__ == '__main__':
    print('Check examples...')

    assert round(sh_1_1_12(1), 7) == 2.0
    assert round(sh_1_1_12(0), 7) == 1.0
    assert round(sh_1_1_12(4), 7) == 2.7083333
    assert round(sh_1_1_12(7), 7) == 2.718254
    assert round(sh_1_1_12(10), 7) == 2.7182818

    print('Done!')
