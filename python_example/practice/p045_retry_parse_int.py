"""
Practice 045. 기본값 있는 정수 변환

난이도: intermediate
수업 순서: 045
학습 주제: 예외처리
관련 기본 예제: basic/a47-a54

문제:
    문자열을 int로 변환하고 실패하면 default를 반환하세요.

예시:
    - ("10", 0) -> 10

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 45
TOPIC = "예외처리"
TITLE = "기본값 있는 정수 변환"


def parse_int_or_default(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    value = args[0]
    default = args[1] if len(args) > 1 else kwargs.get("default", 0)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(parse_int_or_default("10", 0))


if __name__ == "__main__":
    main()
