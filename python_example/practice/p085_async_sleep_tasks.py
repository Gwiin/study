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


def run_async_tasks(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("asyncio 동시 실행 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
