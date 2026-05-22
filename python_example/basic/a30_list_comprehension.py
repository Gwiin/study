import random

def main():
    # 결과 for 변수 in 컨테이너 if 조건
    li = [i**2 for i in range(100) if i % 2 == 0]
    print(li)
    random.shuffle(li)
    print(li)
    print(min(li),max(li),sum(li))
    li.sort()
    print(li)
    li.sort(reverse=True)
    print(li)

if __name__ == "__main__":
    main()

