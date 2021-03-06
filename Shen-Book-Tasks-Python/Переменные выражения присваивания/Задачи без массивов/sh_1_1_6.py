def sh_1_1_6(a: int, b: int) -> int:
    """
        Вычисление суммы а + b (a и b - натуральные).
        Используются операторы присваивания вида
        <переменная1> := <переменная2>,
        <переменная> := <число>,
        <переменная1> := <переменная2> + 1.
    """
    if a < b:
        a, b = b, a

    result, k = a, 0
    while k != b:
        result += 1
        k += 1
    return result


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_6(2, 5) == 2 + 5
    assert sh_1_1_6(5, 2) == 5 + 2
    assert sh_1_1_6(33, 8) == 33 + 8
    assert sh_1_1_6(5, 8) == 5 + 8
    assert sh_1_1_6(4, 0) == 4 + 0
    assert sh_1_1_6(sh_1_1_6(2, 3), sh_1_1_6(2, 4)) == (2 + 3) + (2 + 4)

    print('Done!')
