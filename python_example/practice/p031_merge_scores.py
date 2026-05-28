"""
Practice 031. 점수 병합

난이도: intermediate
수업 순서: 031
학습 주제: 딕셔너리
관련 기본 예제: basic/a25-a77

문제:
    학생별 점수 딕셔너리 2개를 받아 같은 학생은 합산하세요.

예시:
    - ({"a": 10}, {"a": 5, "b": 7}) -> {"a": 15, "b": 7}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 31
TOPIC = "딕셔너리"
TITLE = "점수 병합"


def merge_scores(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    merged = dict(args[0])
    for name, score in dict(args[1]).items():
        merged[name] = merged.get(name, 0) + score
    return merged


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(merge_scores({"a": 10}, {"a": 5, "b": 7}))


if __name__ == "__main__":
    main()
