"""
Practice 021. 1부터 n까지 합

난이도: beginner
수업 순서: 021
학습 주제: 반복문
관련 기본 예제: basic/a21-a30

문제:
    1부터 n까지의 합을 반복문으로 계산하세요. n이 0이면 0입니다.

예시:
    - 10 -> 55

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 21
TOPIC = "반복문"
TITLE = "1부터 n까지 합"


def sum_until(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    n = int(args[0])
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(sum_until(10))


if __name__ == "__main__":
    main()
