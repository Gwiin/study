"""
Practice 002. 영수증 합계 계산

난이도: beginner
수업 순서: 002
학습 주제: 변수/산술연산
관련 기본 예제: basic/a03-a10

문제:
    상품 가격과 수량을 받아 공급가액, 부가세, 총액을 딕셔너리로 반환하세요.

예시:
    - (10000, 3) -> {"subtotal": 30000, "vat": 3000, "total": 33000}
"""

LEVEL = "beginner"
ORDER = 2
TOPIC = "변수/산술연산"
TITLE = "영수증 합계 계산"


def calculate_receipt(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    price, quantity = args
    subtotal = price * quantity
    vat = int(subtotal * 0.1)
    total = subtotal + vat
    return {"subtotal": subtotal, "vat": vat, "total": total}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = 10000, 3
    print(calculate_receipt(*test_data))


if __name__ == "__main__":
    main()
