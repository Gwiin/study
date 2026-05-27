"""
Practice 068. 학생 dataclass

난이도: intermediate
수업 순서: 068
학습 주제: dataclass
관련 기본 예제: basic/a98-a99

문제:
    이름과 점수를 가진 Student dataclass를 만들고 average property를 구현하세요.

예시:
    - Student("kim", [80,90]).average -> 85.0

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 68
TOPIC = "dataclass"
TITLE = "학생 dataclass"


def Student(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("학생 dataclass 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
