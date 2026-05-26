from pathlib import Path
import pickle
from student_model import Student



def main():
    students = []
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.pickle")

    with path.open("rb") as f:
        # try:
        #     while data := pickle.load(f):
        #         students.append(data)
        # except EOFError:
        #     pass
        students = pickle.load(f)
    Student.students = students    
    Student.print()

if __name__ == "__main__":
    main()