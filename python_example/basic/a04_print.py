class A:
    def __repr__(self):
        return "this is Class A -padakmon"

def main():
    print(12345)
    print(1_234_567)
    print("pa dak mon")
    print('python class')
    print(3.141592)
    
    print("this is","python","class")
    print(10,20,30,"hi","fifty")
    print()
    
    print("this is","python","class!!",sep="_", end="")
    print("this is", "python","class", sep="-")
    print(A())
    print(type(A()))

if __name__ == "__main__":
    main()