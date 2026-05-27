"""
Practice 004. 온도 변환기

난이도: beginner
수업 순서: 004
학습 주제: 타입변환
관련 기본 예제: basic/a12

문제:
    섭씨를 화씨와 켈빈으로 변환해 소수점 2자리로 반환하세요.

예시:
    - 25 -> {"fahrenheit": 77.0, "kelvin": 298.15}
"""

LEVEL = "beginner"
ORDER = 4
TOPIC = "타입변환"
TITLE = "온도 변환기"


def convert_temperature(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    celsius = float(args[0])
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    kelvin = round(celsius + 273.15, 2)
    return {"fahrenheit": fahrenheit, "kelvin": kelvin}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    test_data = 25
    print(convert_temperature(test_data))


if __name__ == "__main__":
    main()
