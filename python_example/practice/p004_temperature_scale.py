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

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 4
TOPIC = "타입변환"
TITLE = "온도 변환기"


def convert_temperature(*args, **kwargs):
    """섭씨를 화씨와 켈빈으로 변환해 소수점 2자리로 반환합니다."""
    celsius = float(args[0])
    return {
        "fahrenheit": round(celsius * 9 / 5 + 32, 2),
        "kelvin": round(celsius + 273.15, 2),
    }


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(convert_temperature(25))


if __name__ == "__main__":
    main()
