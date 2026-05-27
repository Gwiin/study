"""
Practice 055. 카운트다운 generator

난이도: intermediate
수업 순서: 055
학습 주제: generator
관련 기본 예제: basic/a44-a45

문제:
    n부터 0까지 내려오는 generator를 만드세요.

예시:
    - list(countdown(3)) -> [3,2,1,0]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 55
TOPIC = "generator"
TITLE = "카운트다운 generator"


def countdown(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("카운트다운 generator 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
