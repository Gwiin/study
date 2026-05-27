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
"""

LEVEL = "beginner"
ORDER = 10
TOPIC = "조건문"
TITLE = "점수 등급 변환"


def score_to_grade(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
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
    test_data = 95
    print(score_to_grade(test_data))


if __name__ == "__main__":
    main()
