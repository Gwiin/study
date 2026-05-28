"""
Practice 022. 구구단 리스트

난이도: beginner
수업 순서: 022
학습 주제: 반복문
관련 기본 예제: basic/a21-a30

문제:
    단을 받아 "2 x 1 = 2" 형식의 9개 문자열 리스트를 반환하세요.

예시:
    - 2 -> 9 lines

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 22
TOPIC = "반복문"
TITLE = "구구단 리스트"


def make_gugudan(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    dan = int(args[0])
    return [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(make_gugudan(2))


if __name__ == "__main__":
    main()
