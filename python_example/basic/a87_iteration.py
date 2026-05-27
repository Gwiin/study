from collections.abc import Iterable

class SimpleIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    print(isinstance(SimpleIter(1, 5), Iterable))

    for i in SimpleIter(1,5):
        print(i)

if __name__ == "__main__":
    main()

# Iterable : for문에서 사용할 수 있는 객체
# iter(객체)를 호출했을 때 iterator를 반환할 수 있으면 Iterable이다.
# Iterator : next()로 값을 하나씩 꺼낼 수 있는 객체
# __next__()에서 더 이상 값이 없으면 StopIteration을 발생시킨다.
# for문은 내부적으로 iter()와 next()를 사용한다.
# SimpleIter는 __iter__(), __next__()를 둘 다 가지고 있어서 for문에서 사용할 수 있다.