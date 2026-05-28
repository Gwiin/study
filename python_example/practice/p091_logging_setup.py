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


import logging


def setup_logger(*args, **kwargs):
    """이름과 레벨을 받아 로거를 설정해 반환합니다."""
    name = args[0] if args else kwargs.get("name", "practice")
    level = kwargs.get("level", logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
        logger.addHandler(handler)
    return logger


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(setup_logger("demo").name)


if __name__ == "__main__":
    main()
