"""
Practice 009. 숫자 분류

난이도: beginner
수업 순서: 009
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    정수를 양수/음수/0, 짝수/홀수로 분류한 문자열을 반환하세요.

예시:
    - -3 -> "negative odd"

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 9
TOPIC = "조건문"
TITLE = "숫자 분류"


def classify_number(*args, **kwargs):
    """정수를 양수/음수/0, 짝수/홀수로 분류합니다."""
    number = int(args[0])
    if number > 0:
        sign = "positive"
    elif number < 0:
        sign = "negative"
    else:
        sign = "zero"
    parity = "even" if number % 2 == 0 else "odd"
    return f"{sign} {parity}"


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(classify_number(-3))


if __name__ == "__main__":
    main()
