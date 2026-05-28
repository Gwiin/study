"""
Practice 068. 학생 dataclass

난이도: intermediate
수업 순서: 068
학습 주제: dataclass
관련 기본 예제: basic/a98-a99

문제:
    이름과 점수를 가진 Student dataclass를 만들고 average property를 구현하세요.

예시:
    - Student("kim", [80,90]).average -> 85.0

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 68
TOPIC = "dataclass"
TITLE = "학생 dataclass"


from dataclasses import dataclass


@dataclass
class Student:
    name: str
    scores: list

    @property
    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0.0


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(Student("kim", [80, 90]).average)


if __name__ == "__main__":
    main()
