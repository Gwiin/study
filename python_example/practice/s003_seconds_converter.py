"""
Practice 003. 초 단위 시간 변환

난이도: beginner
수업 순서: 003
학습 주제: 산술연산
관련 기본 예제: basic/a08-a10

문제:
    초 단위 정수를 시간, 분, 초로 분해하세요.

예시:
    - 3661 -> (1, 1, 1)
"""

LEVEL = "beginner"
ORDER = 3
TOPIC = "산술연산"
TITLE = "초 단위 시간 변환"


def convert_seconds(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    total_seconds = args[0]
    hours = total_seconds // 3600
    remain = total_seconds % 3600
    minutes = remain // 60
    seconds = remain % 60
    return hours, minutes, seconds


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = 3661
    print(convert_seconds(test_data))


if __name__ == "__main__":
    main()
