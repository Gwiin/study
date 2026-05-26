class Student(object): # 상속 문법, object가 이미 숨겨져 있다
    def study(self):
        print("studying")

class Teacher:
    def teach(self):
        print("teaching")


def main():
    student = Student()
    classroom = [Student(), Student(), Teacher(), Student(), Student()]

    print(isinstance(student, Student))
    print(isinstance(student, int))
    print(isinstance(student, object)) # 모든 python의 클래스는 object를 상속받는다.

    print(isinstance(1, object))
    print(isinstance([1, 2, 3, student], object))


    for person in classroom:
        # person.study()
        if isinstance(person,Student):
            person.study()
        if isinstance(person, Teacher):
            person.teach()

if __name__ == "__main__":
    main()