"""
Practice 036. 리스트 묶기

난이도: intermediate
수업 순서: 036
학습 주제: 리스트 슬라이싱
관련 기본 예제: basic/a21-a30

문제:
    리스트를 지정한 크기만큼 묶어 2차원 리스트로 반환하세요.

예시:
    - ([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 36
TOPIC = "리스트 슬라이싱"
TITLE = "리스트 묶기"


def chunk_list(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    items = list(args[0])
    size = int(args[1])
    if size <= 0:
        raise ValueError("청크 크기는 1 이상이어야 합니다.")
    return [items[i:i + size] for i in range(0, len(items), size)]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(chunk_list([1, 2, 3, 4, 5], 2))


if __name__ == "__main__":
    main()
