"""
Practice 005. 원의 넓이와 둘레

난이도: beginner
수업 순서: 005
학습 주제: math 기초
관련 기본 예제: basic/a46

문제:
    반지름을 받아 원의 넓이와 둘레를 계산하세요. pi는 3.14159를 사용하세요.

예시:
    - 10 -> {"area": 314.16, "circumference": 62.83}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 5
TOPIC = "math 기초"
TITLE = "원의 넓이와 둘레"


def circle_metrics(*args, **kwargs):
    """반지름을 받아 원의 넓이와 둘레를 계산합니다."""
    radius = float(args[0])
    pi = 3.14159
    return {
        "area": round(pi * radius * radius, 2),
        "circumference": round(2 * pi * radius, 2),
    }


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(circle_metrics(10))


if __name__ == "__main__":
    main()
