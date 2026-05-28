"""
Practice 085. asyncio 동시 실행

난이도: advanced
수업 순서: 085
학습 주제: asyncio
관련 기본 예제: basic/a105

문제:
    여러 sleep 작업을 동시에 실행하고 결과 리스트를 반환하세요.

예시:
    - await run_async_tasks([...])

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 85
TOPIC = "asyncio"
TITLE = "asyncio 동시 실행"


import asyncio


async def run_async_tasks(*args, **kwargs):
    """비동기 sleep 작업을 동시에 실행하고 이름을 반환합니다."""
    tasks = args[0]

    async def worker(name, delay):
        await asyncio.sleep(delay)
        return name

    return await asyncio.gather(*(worker(name, delay) for name, delay in tasks))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(asyncio.run(run_async_tasks([("a", 0.01), ("b", 0.01)])))


if __name__ == "__main__":
    main()
