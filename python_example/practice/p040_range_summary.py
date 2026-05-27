"""
Practice 040. 범위 요약

난이도: intermediate
수업 순서: 040
학습 주제: range/enumerate
관련 기본 예제: basic/a24

문제:
    정수 리스트를 받아 min, max, count, sum 딕셔너리를 반환하세요. 빈 리스트는 ValueError입니다.

예시:
    - [1,2,3] -> {"min":1,"max":3,"count":3,"sum":6}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 40
TOPIC = "range/enumerate"
TITLE = "범위 요약"


def summarize_numbers(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("범위 요약 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
