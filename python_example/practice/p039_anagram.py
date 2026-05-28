"""
Practice 039. 애너그램 검사

난이도: intermediate
수업 순서: 039
학습 주제: 문자열/정렬
관련 기본 예제: basic/a07-a30

문제:
    두 문자열이 같은 문자 구성인지 확인하세요. 공백과 대소문자는 무시합니다.

예시:
    - ("listen", "silent") -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 39
TOPIC = "문자열/정렬"
TITLE = "애너그램 검사"


def is_anagram(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    left = "".join(str(args[0]).lower().split())
    right = "".join(str(args[1]).lower().split())
    return sorted(left) == sorted(right)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(is_anagram("listen", "silent"))


if __name__ == "__main__":
    main()
