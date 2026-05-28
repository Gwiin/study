"""
Practice 059. JSON 설정 읽기

난이도: intermediate
수업 순서: 059
학습 주제: json/file
관련 기본 예제: basic/a100

문제:
    JSON 파일에서 설정을 읽고 없으면 기본 설정을 반환하세요.

예시:
    - missing path -> default dict

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "intermediate"
ORDER = 59
TOPIC = "json/file"
TITLE = "JSON 설정 읽기"


def load_settings(*args, **kwargs):
    """문제 요구사항에 맞게 구현합니다."""
    import json
    from pathlib import Path

    path = Path(args[0])
    default = args[1] if len(args) > 1 else kwargs.get("default", {})
    if not path.exists():
        return dict(default)
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    return data


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(load_settings("missing.json", {"theme": "light"}))


if __name__ == "__main__":
    main()
