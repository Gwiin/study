class Person:
    def __init__(self,b):
        self.b = b
    def greeting(self):
        print("안녕하세요!")

class University:
    def __init__(self,a):
        self.a = a
    
    def message_credit(self):
        print("학점관리")

class Undergraduate(Person, University):
    def __init__(self): # 다중상속에서는 super가 어떤 부모를 가리키는지 모르기 때문에 아래와 같이 초기화한다.
        Person.__init__(self, 1)
        University.__init__(self,2)
    
    def study(self):
        print("공부하기")

    
def main():
    james = Undergraduate()
    james.greeting()
    james.message_credit()
    james.study()
    print(james.a, james.b)
    print(Undergraduate.__mro__)
    

if __name__ == "__main__":
    main()
    