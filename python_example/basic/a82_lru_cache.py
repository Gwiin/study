from functools import cache, lru_cache

cnt = 0

# @cache
@lru_cache(maxsize=None)
def fibonacci(n):
    global cnt
    cnt += 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    global cnt
    print(fibonacci(36))
    print(f"fibonacci 가 수행된 횟수 {cnt}")

if __name__ == "__main__":
    main()