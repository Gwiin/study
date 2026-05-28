"""
Practice 071. 성적부 클래스

난이도: intermediate
수업 순서: 071
학습 주제: class/list
관련 기본 예제: basic/a61-a72

문제:
    학생별 점수를 저장하고 평균과 최고점을 계산하는 ScoreBook을 구현하세요.

예시:
    - add_score, average, top

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 71
TOPIC = "class/list"
TITLE = "성적부 클래스"


class ScoreBook:
    """학생별 점수를 저장하고 평균과 최고점을 계산합니다."""

    def __init__(self):
        self.scores = {}

    def add_score(self, name, score):
        self.scores.setdefault(name, []).append(score)

    def average(self, name):
        values = self.scores.get(name, [])
        return sum(values) / len(values) if values else 0.0

    def top(self):
        averages = [(name, self.average(name)) for name in self.scores]
        return max(averages, key=lambda item: (item[1], item[0])) if averages else None


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    book = ScoreBook()
    book.add_score("kim", 90)
    book.add_score("lee", 80)
    print(book.top())


if __name__ == "__main__":
    main()
