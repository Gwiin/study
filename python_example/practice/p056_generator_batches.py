"""
Practice 056. 배치 generator

난이도: intermediate
수업 순서: 056
학습 주제: generator
관련 기본 예제: basic/a44-a45

문제:
    리스트와 size를 받아 size 단위 배치를 yield하세요.

예시:
    - list(batches([1,2,3],2)) -> [[1,2],[3]]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 56
TOPIC = "generator"
TITLE = "배치 generator"


def batches(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    items = list(args[0])
    size = int(args[1])
    if size <= 0:
        raise ValueError("배치 크기는 1 이상이어야 합니다.")
    for i in range(0, len(items), size):
        yield items[i:i + size]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(list(batches([1, 2, 3], 2)))


if __name__ == "__main__":
    main()
