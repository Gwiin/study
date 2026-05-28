"""
Practice 044. 정수 리스트 변환

난이도: intermediate
수업 순서: 044
학습 주제: 예외처리
관련 기본 예제: basic/a47-a54

문제:
    문자열 리스트에서 int로 변환 가능한 값만 정수 리스트로 반환하세요.

예시:
    - ["1", "x", "3"] -> [1,3]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 44
TOPIC = "예외처리"
TITLE = "정수 리스트 변환"


def safe_int_list(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    result = []
    for value in args[0]:
        try:
            result.append(int(value))
        except (TypeError, ValueError):
            pass
    return result


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(safe_int_list(["1", "x", "3"]))


if __name__ == "__main__":
    main()
