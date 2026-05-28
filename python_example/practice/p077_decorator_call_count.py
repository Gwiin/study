"""
Practice 077. 호출 횟수 decorator

난이도: advanced
수업 순서: 077
학습 주제: decorator
관련 기본 예제: basic/a101-a103

문제:
    함수 호출 횟수를 기록하는 decorator를 구현하세요.

예시:
    - wrapped.calls increases

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 77
TOPIC = "decorator"
TITLE = "호출 횟수 decorator"


from functools import wraps


def count_calls(func):
    """함수 호출 횟수를 wrapped.calls에 기록하는 데코레이터입니다."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")

    @count_calls
    def hello():
        return "hi"

    hello()
    hello()
    print(hello.calls)


if __name__ == "__main__":
    main()
