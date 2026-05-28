"""
Practice 023. 모음 개수 세기

난이도: beginner
수업 순서: 023
학습 주제: 반복문/문자열
관련 기본 예제: basic/a21-a30

문제:
    영문 문자열에서 a/e/i/o/u 개수를 대소문자 구분 없이 세세요.

예시:
    - "Education" -> 5

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 23
TOPIC = "반복문/문자열"
TITLE = "모음 개수 세기"


def count_vowels(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    text = str(args[0]).lower()
    return sum(1 for char in text if char in "aeiou")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(count_vowels("Education"))


if __name__ == "__main__":
    main()
