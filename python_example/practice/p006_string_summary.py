"""
Practice 006. 문자열 요약

난이도: beginner
수업 순서: 006
학습 주제: 문자열
관련 기본 예제: basic/a07-a14

문제:
    문자열의 길이, 첫 글자, 마지막 글자, 대문자 변환 결과를 반환하세요.

예시:
    - "python" -> {"length": 6, "first": "p", "last": "n", "upper": "PYTHON"}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 6
TOPIC = "문자열"
TITLE = "문자열 요약"


def summarize_text(*args, **kwargs):
    """문자열의 길이, 첫 글자, 마지막 글자, 대문자 변환 결과를 반환합니다."""
    text = str(args[0])
    return {
        "length": len(text),
        "first": text[0] if text else "",
        "last": text[-1] if text else "",
        "upper": text.upper(),
    }


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(summarize_text("python"))


if __name__ == "__main__":
    main()
