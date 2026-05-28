"""
Practice 016. 연령대 구하기

난이도: beginner
수업 순서: 016
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    나이를 받아 10대, 20대처럼 연령대를 반환하세요. 10세 미만은 어린이, 70세 이상은 시니어입니다.

예시:
    - 25 -> "20대"

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 16
TOPIC = "조건문"
TITLE = "연령대 구하기"


def get_age_band(*args, **kwargs):
    """나이를 받아 '20대' 같은 연령대를 반환합니다."""
    age = int(args[0])
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다.")
    return f"{age // 10 * 10}대"


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(get_age_band(25))


if __name__ == "__main__":
    main()
