"""
Practice 047. 키워드 인자 프로필

난이도: intermediate
수업 순서: 047
학습 주제: 함수/**kwargs
관련 기본 예제: basic/a31-a35

문제:
    이름, 나이 등 임의 키워드 인자를 받아 "key=value" 문자열 리스트로 정렬해 반환하세요.

예시:
    - profile_lines(name="kim", age=20) -> ["age=20", "name=kim"]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 47
TOPIC = "함수/**kwargs"
TITLE = "키워드 인자 프로필"


def profile_lines(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("키워드 인자 프로필 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
