def print_n_time(
    *value: str,
    n: int = 2,
    i_var: int = 4,
) -> str:
    """_summary_
    교육용 테스트 함수이다.
    Args:
        value (str): 출력할 메세지
        n (int): 반복 출력횟수

    Returns:
        str: 에러 반환
    """
    print(type(value))
    # temp1, temp2, temp3 = value
    # (temp1, temp2, temp3) = (first, second, third)
    for i in range(n):
        print(value)
        # print("first", temp1, "sencond", temp2, "third", temp3)
        for v in value:
            print(v, end=" ")
        print("\n\n")
    print("i의 값은: ", i_var)
    return "ok"


def print_keyward_arguemnt(a, b, c, d=5, *e):
    print(a, b, c, d, e)


def main():
    return_var = print_n_time("abc", "def", "ghi", "ddd")
    # keyward_argument
    return_var = print_n_time("abc", "def", "ghi", "ddd", n=4)
    return_var = print_n_time("abc", "def", "ghi", "ddd", n=4, i_var=8)
    return_var = print_n_time("abc", "def", "ghi", "ddd", i_var=8, n=4)
    # return_var = "ok"
    print(type(return_var))
    print(*return_var)

    # default_argument
    print_keyward_arguemnt(1, 2, 3, 4, 5, 6, 7)
    print_keyward_arguemnt(1, 2, 3)


if __name__ == "__main__":
    main()