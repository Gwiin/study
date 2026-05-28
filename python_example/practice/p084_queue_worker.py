"""
Practice 084. Queue 작업자

난이도: advanced
수업 순서: 084
학습 주제: threading/queue
관련 기본 예제: basic/a104

문제:
    queue.Queue와 worker thread로 숫자 제곱 결과를 수집하세요.

예시:
    - [1,2,3] -> [1,4,9]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 84
TOPIC = "threading/queue"
TITLE = "Queue 작업자"


from queue import Queue
import threading


def process_queue(*args, **kwargs):
    """큐에 담긴 숫자를 작업자가 제곱해 반환합니다."""
    numbers = list(args[0])
    queue = Queue()
    results = []
    lock = threading.Lock()
    for number in numbers:
        queue.put(number)

    def worker():
        while not queue.empty():
            number = queue.get()
            with lock:
                results.append(number * number)
            queue.task_done()

    thread = threading.Thread(target=worker)
    thread.start()
    queue.join()
    thread.join()
    return results


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(process_queue([1, 2, 3]))


if __name__ == "__main__":
    main()
