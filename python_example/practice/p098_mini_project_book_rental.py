"""
Practice 098. 미니 프로젝트 도서 대여

난이도: advanced
수업 순서: 098
학습 주제: project
관련 기본 예제: 종합 실습

문제:
    도서 등록, 대여, 반납, 연체 목록 조회 기능을 설계하고 구현하세요.

예시:
    - add_book, rent, return_book, overdue

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 98
TOPIC = "project"
TITLE = "미니 프로젝트 도서 대여"


from datetime import date


class BookRental:
    """도서 대여와 반납, 연체 여부를 관리합니다."""

    def __init__(self):
        self.books = {}
        self.rentals = {}

    def add_book(self, title):
        self.books[title] = True

    def rent(self, title, user, due_date):
        if not self.books.get(title, False):
            raise ValueError("대여할 수 없는 책입니다.")
        self.books[title] = False
        self.rentals[title] = {"user": user, "due_date": due_date}

    def return_book(self, title):
        self.books[title] = True
        return self.rentals.pop(title, None)

    def overdue(self, today=None):
        today = today or date.today()
        return [title for title, info in self.rentals.items() if info["due_date"] < today]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    rental = BookRental()
    rental.add_book("Python")
    rental.rent("Python", "kim", date(2026, 5, 1))
    print(rental.overdue(date(2026, 5, 2)))


if __name__ == "__main__":
    main()
