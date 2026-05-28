"""
Practice 037. 리스트 회전

난이도: intermediate
수업 순서: 037
학습 주제: 리스트 슬라이싱
관련 기본 예제: basic/a21-a30

문제:
    리스트를 오른쪽으로 k칸 회전하세요.

예시:
    - ([1,2,3,4], 1) -> [4,1,2,3]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 37
TOPIC = "리스트 슬라이싱"
TITLE = "리스트 회전"


def rotate_right(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    items = list(args[0])
    if not items:
        return []
    count = int(args[1]) % len(items)
    return items[-count:] + items[:-count] if count else items[:]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(rotate_right([1, 2, 3, 4], 1))


if __name__ == "__main__":
    main()
