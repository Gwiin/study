"""
Practice 011. 윤년 판정

난이도: beginner
수업 순서: 011
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    연도를 받아 윤년 여부를 반환하세요.

예시:
    - 2024 -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 11
TOPIC = "조건문"
TITLE = "윤년 판정"


def is_leap_year(*args, **kwargs):
    """연도를 받아 윤년 여부를 반환합니다."""
    year = int(args[0])
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(is_leap_year(2024))


if __name__ == "__main__":
    main()
