from pathlib import Path

def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data")
    # f = open("data/text.txt", "w")
    # f.write("Hello Python Programming...!")
    # f.close()
    with open(path / "text.txt", "a") as f:
        f.write("hello!!!")

if __name__ == "__main__":
    main()


