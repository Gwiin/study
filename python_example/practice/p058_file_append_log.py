"""
Practice 058. 로그 파일 추가

난이도: intermediate
수업 순서: 058
학습 주제: 파일 쓰기
관련 기본 예제: basic/a42-a43

문제:
    로그 파일 경로와 메시지를 받아 타임스탬프 포함 한 줄을 추가하세요.

예시:
    - writes one line

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 58
TOPIC = "파일 쓰기"
TITLE = "로그 파일 추가"


def append_log(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    from pathlib import Path

    path = Path(args[0])
    message = str(args[1])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(message + "\n")
    return str(path)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    from pathlib import Path
    path = Path(__file__).with_suffix(".log")
    print(append_log(path, "hello"))


if __name__ == "__main__":
    main()
