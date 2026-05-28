"""
Practice 026. 평균 점수

난이도: beginner
수업 순서: 026
학습 주제: 리스트
관련 기본 예제: basic/a21-a24

문제:
    점수 리스트의 평균을 소수점 2자리로 반환하세요. 빈 리스트는 0.0입니다.

예시:
    - [80, 90, 100] -> 90.0

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 26
TOPIC = "리스트"
TITLE = "평균 점수"


def average(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    scores = list(args[0])
    return round(sum(scores) / len(scores), 2) if scores else 0.0


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(average([80, 90, 100]))


if __name__ == "__main__":
    main()
