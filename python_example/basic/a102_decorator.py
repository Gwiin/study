from functools import wraps

def hi(value):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"func 실행 전 코드..{value}")
            result = func(*args, **kwargs)
            print(f"func 실행 후 코드..{value}")
            return result
        return wrapper
    return my_decorator


@hi("hi")
def print_hello(n,v):
    for _ in range(n):
        print(v)
    return 123


def main():
    print_hello(5,"hello")
    print(print_hello.__name__)

if __name__ == "__main__":
    main()