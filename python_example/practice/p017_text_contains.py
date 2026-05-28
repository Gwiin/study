"""
Practice 017. 금칙어 검사

난이도: beginner
수업 순서: 017
학습 주제: 문자열/조건문
관련 기본 예제: 관련 예제

문제:
    문장과 금칙어 목록을 받아 금칙어가 포함됐는지 반환하세요. 대소문자는 무시합니다.

예시:
    - ("Hello spam", ["spam"]) -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 17
TOPIC = "문자열/조건문"
TITLE = "금칙어 검사"


def contains_banned_word(*args, **kwargs):
    """문자열에 금지어가 하나라도 포함되어 있으면 True를 반환합니다."""
    text = str(args[0]).lower()
    banned_words = args[1]
    return any(str(word).lower() in text for word in banned_words)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(contains_banned_word("Hello spam", ["spam"]))


if __name__ == "__main__":
    main()
