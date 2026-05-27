"""
Practice 007. 이니셜 만들기

난이도: beginner
수업 순서: 007
학습 주제: 문자열/분기
관련 기본 예제: basic/a07-a20

문제:
    공백으로 구분된 이름에서 각 단어의 첫 글자를 대문자로 모으세요. 빈 문자열은 빈 문자열을 반환하세요.

예시:
    - "bind soft academy" -> "BSA"
"""

LEVEL = "beginner"
ORDER = 7
TOPIC = "문자열/분기"
TITLE = "이니셜 만들기"


def make_initials(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    full_name = str(args[0]).strip()
    if not full_name:
        return ""
    return "".join(part[0].upper() for part in full_name.split())


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = "bind soft academy"
    print(make_initials(test_data))


if __name__ == "__main__":
    main()
