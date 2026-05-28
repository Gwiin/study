"""
Practice 062. 로또 번호 생성

난이도: intermediate
수업 순서: 062
학습 주제: random
관련 기본 예제: basic/a56

문제:
    1~45 중 중복 없는 6개 번호를 오름차순으로 반환하세요. seed를 받으면 재현 가능해야 합니다.

예시:
    - seed=1 -> deterministic list

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 62
TOPIC = "random"
TITLE = "로또 번호 생성"


def generate_lotto(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    import random

    seed = kwargs.get("seed", args[0] if args else None)
    rng = random.Random(seed)
    return sorted(rng.sample(range(1, 46), 6))


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(generate_lotto(seed=1))


if __name__ == "__main__":
    main()
