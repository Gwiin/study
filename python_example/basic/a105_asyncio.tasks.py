import asyncio
import time


async def hello():
    print("hello world!!")
    await asyncio.sleep(5.0)

async def main():
    print("main 함수")
    # await hello()
    t1 = asyncio.create_task(hello()) # t1 함수 시작
    t2 = asyncio.create_task(hello()) # t2 함수 시작
    t3 = asyncio.create_task(hello()) # t3 함수 시작
    await t1 # t1 join
    await t2 # t2 join
    await t3 # t3 join
    print("main 함수 끝")

if __name__ == "__main__":
    asyncio.run(main())