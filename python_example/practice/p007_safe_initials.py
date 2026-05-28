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

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 7
TOPIC = "문자열/분기"
TITLE = "이니셜 만들기"


def make_initials(*args, **kwargs):
    """공백으로 구분된 이름에서 각 단어의 첫 글자를 대문자로 모읍니다."""
    full_name = str(args[0]).strip()
    return "".join(part[0].upper() for part in full_name.split()) if full_name else ""


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(make_initials("bind soft academy"))


if __name__ == "__main__":
    main()
