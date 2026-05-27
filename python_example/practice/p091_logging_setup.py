"""
Practice 091. 로깅 설정

난이도: advanced
수업 순서: 091
학습 주제: logging
관련 기본 예제: basic/a57

문제:
    파일과 콘솔에 동시에 기록하는 logger를 설정하세요.

예시:
    - returns logging.Logger

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 91
TOPIC = "logging"
TITLE = "로깅 설정"


def setup_logger(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("로깅 설정 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
