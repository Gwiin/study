"""
Practice 069. 은행 계좌 클래스

난이도: intermediate
수업 순서: 069
학습 주제: class
관련 기본 예제: basic/a61-a72

문제:
    입금/출금/잔액 조회가 가능한 BankAccount 클래스를 구현하세요.

예시:
    - deposit, withdraw, balance

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 69
TOPIC = "class"
TITLE = "은행 계좌 클래스"


class BankAccount:
    """입금, 출금, 잔액 조회가 가능한 은행 계좌입니다."""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("입금액은 0 이상이어야 합니다.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        self.balance -= amount
        return self.balance


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(300)
    print(account.balance)


if __name__ == "__main__":
    main()
