"""
Practice 061. 확장자별 파일 수

난이도: intermediate
수업 순서: 061
학습 주제: pathlib
관련 기본 예제: basic/a58-a84

문제:
    폴더 경로를 받아 확장자별 파일 개수 딕셔너리를 반환하세요.

예시:
    - folder -> {".py": 3}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 61
TOPIC = "pathlib"
TITLE = "확장자별 파일 수"


def count_extensions(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    from pathlib import Path

    folder = Path(args[0])
    counts = {}
    for path in folder.iterdir():
        if path.is_file():
            ext = path.suffix.lower() or ""
            counts[ext] = counts.get(ext, 0) + 1
    return counts


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    from pathlib import Path
    print(count_extensions(Path(__file__).parent))


if __name__ == "__main__":
    main()
