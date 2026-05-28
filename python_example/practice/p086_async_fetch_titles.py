"""
Practice 086. 비동기 fetch 골격

난이도: advanced
수업 순서: 086
학습 주제: asyncio/aiohttp
관련 기본 예제: basic/a106

문제:
    URL 목록을 받아 HTML title을 비동기로 수집하는 구조를 구현하세요.

예시:
    - requires aiohttp

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 86
TOPIC = "asyncio/aiohttp"
TITLE = "비동기 fetch 골격"


import asyncio
import re


async def fetch_titles(*args, **kwargs):
    """URL 목록의 HTML title을 비동기로 가져옵니다."""
    urls = list(args[0])
    try:
        import aiohttp
    except ImportError as error:
        raise ImportError("aiohttp가 필요합니다.") from error

    async def fetch_one(session, url):
        async with session.get(url) as response:
            html = await response.text()
            match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
            return match.group(1).strip() if match else ""

    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*(fetch_one(session, url) for url in urls))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("aiohttp 설치 후 fetch_titles([...])로 실행하세요.")


if __name__ == "__main__":
    main()
