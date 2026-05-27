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
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("사칙연산 계산기 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
