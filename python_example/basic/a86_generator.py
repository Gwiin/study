def test():
    print("test A")
    # return 0
    yield 0
    print("test B")
    yield 1

def main():
    print("main A")
    generated_func = test()
    print("main B")
    # print(generated_func.__next__())
    print(next(generated_func))
    print(next(generated_func))
    try:
        print(next(generated_func))
    except StopIteration:
        print("generator end")
    print("main C")

    # iterable 한 객체는 foransdmf ehftn dlTEk.
    # __iter__, __next__ 이 두개가 존재하면 iterable

    for re in test():
        print(re)


if __name__ == "__main__":
    main()