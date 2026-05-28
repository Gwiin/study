"""
Practice 041. 이메일 간단 검증

난이도: intermediate
수업 순서: 041
학습 주제: 문자열/조건문
관련 기본 예제: 관련 예제

문제:
    문자열에 @가 하나 있고, @ 뒤에 점이 있으면 True를 반환하세요.

예시:
    - "a@b.com" -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 41
TOPIC = "문자열/조건문"
TITLE = "이메일 간단 검증"


def is_valid_email(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    email = str(args[0])
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    return bool(local) and "." in domain and not domain.startswith(".") and not domain.endswith(".")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(is_valid_email("a@b.com"))


if __name__ == "__main__":
    main()
