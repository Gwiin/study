"""
Practice 064. 환경변수 읽기

난이도: intermediate
수업 순서: 064
학습 주제: os
관련 기본 예제: basic/a58

문제:
    환경변수 이름과 기본값을 받아 값을 반환하세요.

예시:
    - missing -> default

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 64
TOPIC = "os"
TITLE = "환경변수 읽기"


def get_env(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    import os

    key = str(args[0])
    default = args[1] if len(args) > 1 else kwargs.get("default")
    return os.environ.get(key, default)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(get_env("MISSING_ENV", "default"))


if __name__ == "__main__":
    main()
