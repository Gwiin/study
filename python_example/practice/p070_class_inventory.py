"""
Practice 070. 재고 관리 클래스

난이도: intermediate
수업 순서: 070
학습 주제: class/dict
관련 기본 예제: basic/a61-a77

문제:
    상품 입고/출고/조회 기능을 가진 Inventory 클래스를 구현하세요.

예시:
    - add, remove, get_stock

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 70
TOPIC = "class/dict"
TITLE = "재고 관리 클래스"


class Inventory:
    """상품별 재고를 관리합니다."""

    def __init__(self):
        self.items = {}

    def add(self, name, quantity):
        self.items[name] = self.items.get(name, 0) + quantity
        return self.items[name]

    def remove(self, name, quantity):
        if self.get_stock(name) < quantity:
            raise ValueError("재고가 부족합니다.")
        self.items[name] -= quantity
        return self.items[name]

    def get_stock(self, name):
        return self.items.get(name, 0)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    inventory = Inventory()
    inventory.add("pen", 5)
    inventory.remove("pen", 2)
    print(inventory.get_stock("pen"))


if __name__ == "__main__":
    main()
