"""
Practice 095. 미니 프로젝트 출석부

난이도: advanced
수업 순서: 095
학습 주제: project
관련 기본 예제: 종합 실습

문제:
    학생 출석 상태를 기록하고 결석자 목록과 출석률을 계산하세요.

예시:
    - mark, absentees, rate

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 95
TOPIC = "project"
TITLE = "미니 프로젝트 출석부"


class AttendanceBook:
    """학생 출석 여부를 관리합니다."""

    def __init__(self, students):
        self.students = list(students)
        self.records = {student: False for student in self.students}

    def mark(self, student, present=True):
        if student not in self.records:
            raise ValueError("등록되지 않은 학생입니다.")
        self.records[student] = present

    def absentees(self):
        return [student for student, present in self.records.items() if not present]

    def rate(self):
        if not self.records:
            return 0.0
        present = sum(1 for value in self.records.values() if value)
        return present / len(self.records)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    book = AttendanceBook(["kim", "lee"])
    book.mark("kim")
    print(book.absentees())
    print(book.rate())


if __name__ == "__main__":
    main()
