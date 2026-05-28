"""
Practice 020. 문자 박스 만들기

난이도: beginner
수업 순서: 020
학습 주제: 반복문 기초
관련 기본 예제: basic/a21-a30

문제:
    문자와 너비를 받아 해당 문자로 구성된 한 줄 문자열을 만드세요.

예시:
    - ("=", 5) -> "====="

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 20
TOPIC = "반복문 기초"
TITLE = "문자 박스 만들기"


def make_line(*args, **kwargs):
    """문자와 길이를 받아 해당 문자를 반복한 문자열을 반환합니다."""
    char = str(args[0])
    length = int(args[1])
    return char * length


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(make_line("=", 5))


if __name__ == "__main__":
    main()
