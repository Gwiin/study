from dataclasses import dataclass


@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int

    def get_sum(self):
        return self.korean + self.math + self.english + self.science


def main():
    students = [
        Student("abc", 34, 65, 35, 94),
        Student("gdf", 34, 45, 45, 50),
        Student("wtr", 36, 75, 63, 94),
        Student("nbd", 47, 65, 85, 70),
        Student("ujd", 88, 95, 75, 33),
        Student("efg", 64, 65, 55, 40),
        Student("dgd", 33, 25, 75, 93),
    ]
    print(students[0])
    print(students[0].get_sum())


if __name__ == "__main__":
    main()

