"""
Practice 049. 팩토리얼 재귀

난이도: intermediate
수업 순서: 049
학습 주제: 재귀
관련 기본 예제: basic/a36-a82

문제:
    재귀로 n!을 계산하세요. 음수는 ValueError입니다.

예시:
    - 5 -> 120

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 49
TOPIC = "재귀"
TITLE = "팩토리얼 재귀"


def factorial(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    n = int(args[0])
    if n < 0:
        raise ValueError("음수의 팩토리얼은 계산할 수 없습니다.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(factorial(5))


if __name__ == "__main__":
    main()
