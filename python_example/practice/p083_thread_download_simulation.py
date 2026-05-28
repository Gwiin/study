"""
Practice 083. 스레드 작업 시뮬레이션

난이도: advanced
수업 순서: 083
학습 주제: threading
관련 기본 예제: basic/a104

문제:
    여러 작업 시간을 받아 Thread로 동시에 실행하고 완료 순서를 기록하세요.

예시:
    - durations -> completed names

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 83
TOPIC = "threading"
TITLE = "스레드 작업 시뮬레이션"


import threading
import time


def run_tasks(*args, **kwargs):
    """작업 이름과 대기 시간을 스레드로 처리하고 완료된 이름을 반환합니다."""
    tasks = args[0]
    completed = []
    lock = threading.Lock()

    def worker(name, duration):
        time.sleep(duration)
        with lock:
            completed.append(name)

    threads = [threading.Thread(target=worker, args=task) for task in tasks]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return completed


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(run_tasks([("a", 0.01), ("b", 0.01)]))


if __name__ == "__main__":
    main()
