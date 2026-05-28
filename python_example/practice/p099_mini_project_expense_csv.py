"""
Practice 099. 미니 프로젝트 CSV 지출 분석

난이도: advanced
수업 순서: 099
학습 주제: project/file
관련 기본 예제: 종합 실습

문제:
    CSV 지출 내역을 읽어 월별/카테고리별 합계를 계산하세요.

예시:
    - load, monthly_summary, category_summary

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 99
TOPIC = "project/file"
TITLE = "미니 프로젝트 CSV 지출 분석"


import csv
from collections import defaultdict
from pathlib import Path


class ExpenseAnalyzer:
    """CSV 지출 내역을 월별/카테고리별로 요약합니다."""

    def __init__(self, path=None):
        self.rows = []
        if path is not None:
            self.load(path)

    def load(self, path):
        with Path(path).open(newline="", encoding="utf-8") as file:
            self.rows = list(csv.DictReader(file))
        return self.rows

    def monthly_summary(self):
        summary = defaultdict(float)
        for row in self.rows:
            month = row["date"][:7]
            summary[month] += float(row["amount"])
        return dict(summary)

    def category_summary(self):
        summary = defaultdict(float)
        for row in self.rows:
            summary[row["category"]] += float(row["amount"])
        return dict(summary)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    path = Path(__file__).with_suffix(".sample.csv")
    path.write_text("date,category,amount\n2026-05-01,food,1000\n", encoding="utf-8")
    analyzer = ExpenseAnalyzer(path)
    print(analyzer.monthly_summary())


if __name__ == "__main__":
    main()
