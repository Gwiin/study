"""
Practice 093. 미니 프로젝트 예산 관리

난이도: advanced
수업 순서: 093
학습 주제: project
관련 기본 예제: 종합 실습

문제:
    수입/지출 항목을 등록하고 카테고리별 합계를 계산하는 구조를 구현하세요.

예시:
    - add_income, add_expense, summary

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 93
TOPIC = "project"
TITLE = "미니 프로젝트 예산 관리"


class BudgetBook:
    """수입과 지출을 기록하고 요약합니다."""

    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, memo=""):
        self.incomes.append((amount, memo))

    def add_expense(self, amount, memo=""):
        self.expenses.append((amount, memo))

    def summary(self):
        income = sum(amount for amount, _ in self.incomes)
        expense = sum(amount for amount, _ in self.expenses)
        return {"income": income, "expense": expense, "balance": income - expense}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    book = BudgetBook()
    book.add_income(10000)
    book.add_expense(3000)
    print(book.summary())


if __name__ == "__main__":
    main()
