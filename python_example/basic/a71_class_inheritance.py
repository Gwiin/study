class Parent:
    def __init__(self,value):
        self.value = "테스트"
        self.value2 = value
        print("Parent 클래스의 __init__ 메소드가 호출 되었다.")
    
    def test(self, *args):
        print("Parent 클래스의 test 메소드 입니다.")

class Child(Parent):
    def __init__(self, value):
        super().__init__(value)
        print("Child 클래스의 __init__ 메소드가 호출 되었다.")
    
    # 파이썬에서는 오버로딩이 없다. 오버라이딩만 된다. -> 특수한 overloading 데코레이터를 사용하면 구현할 수 는 있다.
    def test(self, *args):
        print("Child 클래스의 test 메소드 입니다.")


def main():
    pObject = Parent("부모 자료")
    pObject.test()

    child = Child("자식 자료")
    child.test()
    print(child.value)
    print(child.value2)


if __name__ == "__main__":
    main()

