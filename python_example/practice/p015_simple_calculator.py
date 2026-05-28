"""
Practice 015. 사칙연산 계산기

난이도: beginner
수업 순서: 015
학습 주제: 조건문/함수
관련 기본 예제: basic/a18-a31

문제:
    두 수와 연산자 문자열(+,-,*,/)을 받아 계산 결과를 반환하세요. 0으로 나누기는 ValueError입니다.

예시:
    - (10, 2, "+") -> 12

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 15
TOPIC = "조건문/함수"
TITLE = "사칙연산 계산기"


def calculate(*args, **kwargs):
    """두 숫자와 연산자(+,-,*,/)를 받아 계산 결과를 반환합니다."""
    left = float(args[0])
    right = float(args[1])
    operator = str(args[2])
    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    elif operator == "/":
        if right == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        result = left / right
    else:
        raise ValueError("지원하지 않는 연산자입니다.")
    return int(result) if result.is_integer() else result


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(calculate(10, 2, "+"))


if __name__ == "__main__":
    main()
