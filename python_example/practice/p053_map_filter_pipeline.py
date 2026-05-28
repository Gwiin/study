"""
Practice 053. map/filter 파이프라인

난이도: intermediate
수업 순서: 053
학습 주제: map/filter
관련 기본 예제: basic/a40-a41

문제:
    숫자 리스트에서 양수만 골라 제곱한 리스트를 반환하세요.

예시:
    - [-2,3,0,4] -> [9,16]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 53
TOPIC = "map/filter"
TITLE = "map/filter 파이프라인"


def positive_squares(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    return list(map(lambda number: number * number, filter(lambda number: number > 0, args[0])))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(positive_squares([-2, 3, 0, 4]))


if __name__ == "__main__":
    main()
