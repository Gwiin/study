"""
Practice 029. 단어 길이 사전

난이도: beginner
수업 순서: 029
학습 주제: 딕셔너리
관련 기본 예제: basic/a25-a77

문제:
    단어 리스트를 받아 단어별 길이 딕셔너리를 만드세요.

예시:
    - ["python", "ai"] -> {"python": 6, "ai": 2}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 29
TOPIC = "딕셔너리"
TITLE = "단어 길이 사전"


def word_lengths(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    return {word: len(word) for word in args[0]}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(word_lengths(["python", "ai"]))


if __name__ == "__main__":
    main()
