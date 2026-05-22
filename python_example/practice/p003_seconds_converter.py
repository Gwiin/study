"""
Practice 003. 초 단위 시간 변환

난이도: beginner
수업 순서: 003
학습 주제: 산술연산
관련 기본 예제: basic/a08-a10

문제:
    초 단위 정수를 시간, 분, 초로 분해하세요.

예시:
    - 3661 -> (1, 1, 1)

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 3
TOPIC = "산술연산"
TITLE = "초 단위 시간 변환"


def convert_seconds(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    total_seconds = args[0] if args else kwargs["seconds"]
    hours = int(total_seconds/3600)
    seconds = total_seconds%3600
    minutes = int(seconds/60)
    seconds = int(seconds%60)
    # minutes, seconds = divmod(total_seconds, 60)
    # hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")
    print(convert_seconds(3661))


if __name__ == "__main__":
    main()
