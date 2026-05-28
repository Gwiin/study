"""
Practice 038. 회문 검사

난이도: intermediate
수업 순서: 038
학습 주제: 문자열/리스트
관련 기본 예제: basic/a07-a30

문제:
    공백과 대소문자를 무시하고 회문 여부를 반환하세요.

예시:
    - "A man a plan a canal Panama" -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 38
TOPIC = "문자열/리스트"
TITLE = "회문 검사"


def is_palindrome(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    cleaned = "".join(char.lower() for char in str(args[0]) if char.isalnum())
    return cleaned == cleaned[::-1]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(is_palindrome("A man a plan a canal Panama"))


if __name__ == "__main__":
    main()
