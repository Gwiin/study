"""
Practice 072. 벡터 special method

난이도: advanced
수업 순서: 072
학습 주제: special method
관련 기본 예제: basic/a66

문제:
    2D Vector 클래스에 +, -, ==, repr을 구현하세요.

예시:
    - Vector(1,2)+Vector(3,4) == Vector(4,6)

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 72
TOPIC = "special method"
TITLE = "벡터 special method"


from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(Vector(1, 2) + Vector(3, 4))


if __name__ == "__main__":
    main()
