import json
from pathlib import Path

def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.json")

    with path.open("r", encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        print(type(data))
        

if __name__ == "__main__":
    main()