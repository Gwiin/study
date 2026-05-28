"""
Practice 012. 배송비 계산

난이도: beginner
수업 순서: 012
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    주문금액과 회원 여부를 받아 배송비를 계산하세요. 5만원 이상 또는 회원이면 무료, 아니면 3000원입니다.

예시:
    - (40000, False) -> 3000

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 12
TOPIC = "조건문"
TITLE = "배송비 계산"


def calculate_shipping_fee(*args, **kwargs):
    """주문금액과 회원 여부를 받아 배송비를 계산합니다."""
    amount = int(args[0])
    is_member = bool(args[1])
    return 0 if amount >= 50000 or is_member else 3000


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(calculate_shipping_fee(40000, False))


if __name__ == "__main__":
    main()
