"""
Practice 052. 람다 정렬

난이도: intermediate
수업 순서: 052
학습 주제: lambda/sort
관련 기본 예제: basic/a40-a41

문제:
    (이름, 점수) 튜플 리스트를 점수 내림차순, 이름 오름차순으로 정렬하세요.

예시:
    - [("b",90),("a",90)] -> [("a",90),("b",90)]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 52
TOPIC = "lambda/sort"
TITLE = "람다 정렬"


def sort_scores(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    return sorted(args[0], key=lambda item: (-item[1], item[0]))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(sort_scores([("b", 90), ("a", 90)]))


if __name__ == "__main__":
    main()
