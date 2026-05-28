"""
Practice 075. 주문-상품 합성

난이도: advanced
수업 순서: 075
학습 주제: composition
관련 기본 예제: basic/a98-a99

문제:
    Product와 OrderItem, Order 클래스를 만들고 주문 총액을 계산하세요.

예시:
    - order.total -> sum

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 75
TOPIC = "composition"
TITLE = "주문-상품 합성"


from dataclasses import dataclass


@dataclass
class OrderItem:
    name: str
    price: int
    quantity: int = 1

    @property
    def subtotal(self):
        return self.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append(OrderItem(name, price, quantity))

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    order = Order()
    order.add_item("book", 10000, 2)
    print(order.total)


if __name__ == "__main__":
    main()
