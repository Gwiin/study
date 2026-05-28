"""
Practice 032. 최고점 학생

난이도: intermediate
수업 순서: 032
학습 주제: 딕셔너리/정렬
관련 기본 예제: basic/a25-a77

문제:
    학생 점수 딕셔너리에서 최고점 학생 이름과 점수를 반환하세요. 동점이면 이름 오름차순 첫 번째입니다.

예시:
    - {"kim": 90, "lee": 90} -> ("kim", 90)

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 32
TOPIC = "딕셔너리/정렬"
TITLE = "최고점 학생"


def top_student(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    scores = dict(args[0])
    if not scores:
        raise ValueError("점수 딕셔너리가 비어 있습니다.")
    name = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[0]
    return name


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(top_student({"kim": 90, "lee": 90}))


if __name__ == "__main__":
    main()
