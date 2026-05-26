from pathlib import Path
import sys

def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data")
    with open(path / "text.txt", "r") as f:
        # data = f.readlines()
        # print(data)
        # for str in data:
        #     print(str)

        # data = f.read()
        # print(data)

        # 파일이 굉장히 클때.
        while data := f.readline():
            print(data)

    
    print(sys.stdin.fileno())
    print(sys.stdout.fileno())
    print(sys.stderr.fileno())
    print("error message", file = sys.stderr)

    with open(path / "text.txt", "a", encoding="utf-8") as f:
        print("이것은 프린트로 파일을 쓴 데이터이다.", file=f)


if __name__ == "__main__":
    main()