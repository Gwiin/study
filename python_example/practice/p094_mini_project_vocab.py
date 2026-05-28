"""
Practice 094. 미니 프로젝트 단어장

난이도: advanced
수업 순서: 094
학습 주제: project
관련 기본 예제: 종합 실습

문제:
    단어 추가, 검색, 퀴즈 출제가 가능한 VocabularyBook을 구현하세요.

예시:
    - add, search, quiz

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 94
TOPIC = "project"
TITLE = "미니 프로젝트 단어장"


import random


class VocabularyBook:
    """단어를 추가, 검색, 퀴즈로 사용할 수 있는 단어장입니다."""

    def __init__(self):
        self.words = {}

    def add(self, word, meaning):
        self.words[word] = meaning

    def search(self, word):
        return self.words.get(word)

    def quiz(self, seed=None):
        if not self.words:
            return None
        rng = random.Random(seed)
        word = rng.choice(list(self.words.keys()))
        return word, self.words[word]


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    book = VocabularyBook()
    book.add("apple", "사과")
    print(book.quiz(seed=1))


if __name__ == "__main__":
    main()
