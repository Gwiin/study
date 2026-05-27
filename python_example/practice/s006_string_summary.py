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
"""

LEVEL = "beginner"
ORDER = 6
TOPIC = "문자열"
TITLE = "문자열 요약"


def summarize_text(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    text = str(args[0])
    if text:
        first = text[0]
        last = text[-1]
    else:
        first = ""
        last = ""
    return {"length": len(text), "first": first, "last": last, "upper": text.upper()}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = "python"
    print(summarize_text(test_data))


if __name__ == "__main__":
    main()
