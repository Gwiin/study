"""
Practice 080. 양수 descriptor

난이도: advanced
수업 순서: 080
학습 주제: descriptor
관련 기본 예제: basic/a100

문제:
    속성에 양수만 저장되게 하는 PositiveNumber descriptor를 구현하세요.

예시:
    - negative assignment raises ValueError

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 80
TOPIC = "descriptor"
TITLE = "양수 descriptor"


class PositiveNumber:
    """음수 대입을 막는 디스크립터입니다."""

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("0 이상의 숫자만 저장할 수 있습니다.")
        setattr(instance, self.private_name, value)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")

    class Product:
        price = PositiveNumber()

    product = Product()
    product.price = 100
    print(product.price)


if __name__ == "__main__":
    main()
