import random
from pathlib import Path
import pickle

class Student:
    count = int()
    students = list()

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
        self.__aa = "secret key"

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}"

    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t\
            {self.get_sum()}\t {self.get_average()}"

    def __str__(self) -> str:
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"

    # 사칙연산 + - * /
    def __add__(self, other):
        return self.get_sum() + other.get_sum()

    def __sub__(self, other):
        return self.get_sum() - other.get_sum()

    def __mul__(self, other):
        return self.get_sum() * other.get_sum()

    def __truediv__(self, other):
        return self.get_sum() / other.get_sum()

    # 관계 연산자 greater than -> gt , less than -> lt, equal -> eq, nagative ->ne
    # grather than equal -> ge, less than equal ->le
    def __gt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        else:
            # raise
            return "error"

    @classmethod
    def print(cls):
        print(f"등록된 학생 수는 {Student.count}")
        print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")
        print()
        print("--------------------학생 목록--------------------------")
        for student in Student.students:
            print(student)
        print("-------------------------------------------------------")


def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.pickle")
    hanguls = list("최강박이손정적고구류오김송곽유")
    hanguls2 = list("가나다라마바사아자차카타파하길진재형준석화섭윤진귀용수도윤경")
    students = [
        Student(
            random.choice(hanguls) + "".join(random.choices(hanguls2, k=2)),
            random.randint(65,100),
            random.randint(65,100),
            random.randint(65,100),
            random.randint(65,100)
        )
        for _ in range(100) 
    ]
    Student.print()

    with path.open("wb") as f:
        pickle.dump(students, f)



if __name__ == "__main__":
    main()