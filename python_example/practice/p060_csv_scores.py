"""
Practice 060. CSV 점수 평균

난이도: intermediate
수업 순서: 060
학습 주제: csv/file
관련 기본 예제: basic/a42-a43

문제:
    name,score 형식 CSV 파일을 읽어 평균 점수를 반환하세요.

예시:
    - csv path -> float

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 60
TOPIC = "csv/file"
TITLE = "CSV 점수 평균"


def average_csv_score(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    import csv
    from pathlib import Path

    path = Path(args[0])
    scores = []
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores.append(float(row.get("score", 0)))
    return sum(scores) / len(scores) if scores else 0.0


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    from pathlib import Path
    path = Path(__file__).with_suffix(".sample.csv")
    path.write_text("name,score\nkim,90\nlee,80\n", encoding="utf-8")
    print(average_csv_score(path))


if __name__ == "__main__":
    main()
