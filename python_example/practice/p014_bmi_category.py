"""
Practice 014. BMI 분류

난이도: beginner
수업 순서: 014
학습 주제: 조건문/계산
관련 기본 예제: basic/a18-a20

문제:
    키(cm)와 몸무게(kg)를 받아 BMI와 분류 문자열을 반환하세요.

예시:
    - (170, 65) -> (22.49, "normal")

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 14
TOPIC = "조건문/계산"
TITLE = "BMI 분류"


def classify_bmi(*args, **kwargs):
    """키(cm)와 몸무게(kg)를 받아 BMI와 분류를 반환합니다."""
    height_cm = float(args[0])
    weight_kg = float(args[1])
    bmi = round(weight_kg / ((height_cm / 100) ** 2), 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 23:
        category = "normal"
    elif bmi < 25:
        category = "overweight"
    else:
        category = "obese"
    return bmi, category


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(classify_bmi(170, 65))


if __name__ == "__main__":
    main()
