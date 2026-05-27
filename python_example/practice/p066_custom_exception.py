"""
Practice 066. 커스텀 예외

난이도: intermediate
수업 순서: 066
학습 주제: 예외처리
관련 기본 예제: basic/a47-a54

문제:
    잔액보다 큰 출금 요청이면 InsufficientBalanceError를 발생시키세요.

예시:
    - (1000, 500) -> 500

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 66
TOPIC = "예외처리"
TITLE = "커스텀 예외"


def withdraw(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("커스텀 예외 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
