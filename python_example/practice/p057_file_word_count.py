"""
Practice 057. 파일 단어 수

난이도: intermediate
수업 순서: 057
학습 주제: 파일 읽기
관련 기본 예제: basic/a42-a43

문제:
    텍스트 파일 경로를 받아 단어 수를 반환하세요. 파일이 없으면 0입니다.

예시:
    - path -> integer

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 57
TOPIC = "파일 읽기"
TITLE = "파일 단어 수"


def count_file_words(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    from pathlib import Path

    path = Path(args[0])
    text = path.read_text(encoding="utf-8")
    return len(text.split())


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    from pathlib import Path
    path = Path(__file__)
    print(count_file_words(path))


if __name__ == "__main__":
    main()
