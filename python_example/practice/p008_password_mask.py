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

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 8
TOPIC = "문자열 슬라이싱"
TITLE = "비밀번호 마스킹"


def mask_password(*args, **kwargs):
    """문자열 앞 2글자만 남기고 나머지는 *로 바꿉니다."""
    password = str(args[0])
    if len(password) <= 2:
        return password
    return password[:2] + "*" * (len(password) - 2)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(mask_password("abcdef"))


if __name__ == "__main__":
    main()
