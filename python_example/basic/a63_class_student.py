class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"
    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"


def main():
    students = [
        Student('abc',34,65,35,94),
        Student('gdf',34,45,45,50),
        Student('wtr',36,75,63,94),
        Student('nbd',47,65,85,70),
        Student('ujd',88,95,75,33),
        Student('efg',64,65,55,40),
        Student('dgd',33,25,75,93)
    ]
    # print(students)
    # print(students[0])
    print("이름\t 국어\t 수학\t 영어\t 과학\t 총합\t 평균")
    for student in students:
        # print(student.to_string())
        print(student)


if __name__ == "__main__":
    main()