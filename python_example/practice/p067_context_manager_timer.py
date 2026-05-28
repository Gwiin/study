"""
Practice 067. 실행 시간 context manager

난이도: advanced
수업 순서: 067
학습 주제: context manager
관련 기본 예제: basic/a42-a52

문제:
    with 문에서 사용할 수 있는 간단한 Timer 클래스를 구현하세요.

예시:
    - with Timer() as t: ...

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 67
TOPIC = "context manager"
TITLE = "실행 시간 context manager"


import time


class Timer:
    """with 문에서 실행 시간을 측정하는 컨텍스트 매니저입니다."""

    def __enter__(self):
        self.start = time.perf_counter()
        self.elapsed = 0.0
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return False


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    with Timer() as timer:
        sum(range(1000))
    print(timer.elapsed >= 0)


if __name__ == "__main__":
    main()
