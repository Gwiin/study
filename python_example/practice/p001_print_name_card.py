"""
Practice 001. 이름표 출력하기

난이도: beginner
수업 순서: 001
학습 주제: 출력/문자열
관련 기본 예제: basic/a01-a07

문제:
    이름, 과정명, 날짜를 받아 3줄짜리 이름표 문자열을 만드세요.

예시:
    - ("홍길동", "Python", "2026-05-20") -> "이름: 홍길동\n과정: Python\n날짜: 2026-05-20"

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 1
TOPIC = "출력/문자열"
TITLE = "이름표 출력하기"


def build_name_card(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    name, subject, date = args
    print(f"이름: {name}\n과정: {subject}\n날짜: {date}")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")

    test_data = "홍길동", "Python", "2026-05-20"
    build_name_card(*test_data)


if __name__ == "__main__":
    main()
