"""
Practice 073. 사각형 property

난이도: advanced
수업 순서: 073
학습 주제: property
관련 기본 예제: basic/a70

문제:
    width/height가 양수만 허용되도록 property를 구현하세요. area도 제공합니다.

예시:
    - Rectangle(3,4).area -> 12

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 73
TOPIC = "property"
TITLE = "사각형 property"


class Rectangle:
    """너비와 높이로 넓이와 둘레를 계산합니다."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(Rectangle(3, 4).area)


if __name__ == "__main__":
    main()
