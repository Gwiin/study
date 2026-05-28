"""
Practice 081. 연락처 pickle 저장

난이도: advanced
수업 순서: 081
학습 주제: pickle/file
관련 기본 예제: basic/a96-a97

문제:
    연락처 리스트를 pickle로 저장하고 다시 읽는 함수를 구현하세요.

예시:
    - save_contacts, load_contacts

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 81
TOPIC = "pickle/file"
TITLE = "연락처 pickle 저장"


import pickle
from pathlib import Path


def save_contacts(path, contacts):
    path = Path(path)
    with path.open("wb") as file:
        pickle.dump(contacts, file)


def load_contacts(path):
    path = Path(path)
    with path.open("rb") as file:
        return pickle.load(file)


def save_load_contacts(*args, **kwargs):
    """연락처를 pickle로 저장한 뒤 다시 읽어 반환합니다."""
    path = args[0]
    contacts = args[1]
    save_contacts(path, contacts)
    return load_contacts(path)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    path = Path(__file__).with_suffix(".pkl")
    print(save_load_contacts(path, {"kim": "010"}))


if __name__ == "__main__":
    main()
