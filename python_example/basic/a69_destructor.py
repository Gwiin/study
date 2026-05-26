class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}이 생성 되었습니다.")

    def __del__(self):
        print(f"{self.name}이 파괴 되었습니다.")

    # def __new__(self):

def main():
    a = Test("a")
    b = Test("b")
    c = Test("c")
    print(a, b, c)
    del c

if __name__ == "__main__":
    main()