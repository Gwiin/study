"""
Practice 010. 점수 등급 변환

난이도: beginner
수업 순서: 010
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    0~100 점수를 A/B/C/D/F 등급으로 변환하세요. 범위 밖이면 ValueError를 발생시키세요.

예시:
    - 95 -> "A"

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 10
TOPIC = "조건문"
TITLE = "점수 등급 변환"


def score_to_grade(*args, **kwargs):
    """0~100 점수를 A/B/C/D/F 등급으로 변환합니다."""
    score = float(args[0])
    if score < 0 or score > 100:
        raise ValueError("점수는 0~100 범위여야 합니다.")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(score_to_grade(95))


if __name__ == "__main__":
    main()
