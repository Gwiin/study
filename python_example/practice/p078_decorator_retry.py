"""
Practice 078. 재시도 decorator

난이도: advanced
수업 순서: 078
학습 주제: decorator
관련 기본 예제: basic/a101-a103

문제:
    예외 발생 시 지정 횟수만큼 재시도하는 decorator를 구현하세요.

예시:
    - @retry(times=3)

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 78
TOPIC = "decorator"
TITLE = "재시도 decorator"


from functools import wraps


def retry(*args, **kwargs):
    """실패한 함수를 지정 횟수만큼 재시도하는 데코레이터를 만듭니다."""
    times = kwargs.get("times", args[0] if args else 3)

    def decorator(func):
        @wraps(func)
        def wrapper(*f_args, **f_kwargs):
            last_error = None
            for _ in range(times):
                try:
                    return func(*f_args, **f_kwargs)
                except Exception as error:
                    last_error = error
            raise last_error

        return wrapper

    return decorator


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")

    @retry(times=3)
    def ok():
        return "done"

    print(ok())


if __name__ == "__main__":
    main()
