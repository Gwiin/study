from functools import wraps
import time

def runtime_check(n):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"{func.__name__}지금부터 {n}번 실행 평균 표시")
            start_time = time.time()
            for i in range(n):
                result = func(*args, **kwargs)
            end_time = time.time()
            print(f"실행 시간은 {(end_time-start_time)/n:.3} 입니다")
            return result
        return wrapper
    return my_decorator


@runtime_check(10)
def print_hello(n,s):
    for _ in range(n):
        s += 1
    return s


def main():
    re = print_hello(50_000_000, 10_000_000)
    print(re)

if __name__ == "__main__":
    main()