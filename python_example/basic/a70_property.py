import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    # Descriptor -> attr, getattr, setattr, delattr
    @property # 형태는 메소드이지만 사용은 인스턴스 변수처럼
    def radius(self):
        return self.__radius
    
    @radius.getter
    def radius(self):
        print("getter")
        return self.__radius
    
    @radius.setter
    def radius(self,value):
        print("setter")
        if isinstance(value, int) and value > 0:
            self.__radius = value
        else:
            print("양의 정수만 넣으시오.")

    def get_area(self):
        return math.pi * (self.__radius**2)


def main():
    circle = Circle(10)
    print(circle.radius)
    circle.radius = 20
    circle.radius = 3.14
    circle.radius = -5
    print(circle.get_area())
    
    # descriptor
    print(circle.__dict__)
    print(vars(circle))
    print(getattr(circle, "get_area"))
    print(getattr(circle, "get_area")())
    print(getattr(circle, "get_area2", None))



if __name__ == "__main__":
    main()