"""
Practice 008. 비밀번호 마스킹

난이도: beginner
수업 순서: 008
학습 주제: 문자열 슬라이싱
관련 기본 예제: basic/a07

문제:
    문자열 앞 2글자만 남기고 나머지는 *로 바꾸세요. 길이가 2 이하이면 그대로 반환하세요.

예시:
    - "abcdef" -> "ab****"
"""

LEVEL = "beginner"
ORDER = 8
TOPIC = "문자열 슬라이싱"
TITLE = "비밀번호 마스킹"


def mask_password(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    password = str(args[0])
    if len(password) <= 2:
        return password
    return password[:2] + ("*" * (len(password) - 2))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = "abcdef"
    print(mask_password(test_data))


if __name__ == "__main__":
    main()
