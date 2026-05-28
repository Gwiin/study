"""
Practice 090. CLI 인자 파서

난이도: advanced
수업 순서: 090
학습 주제: argparse
관련 기본 예제: basic/a57

문제:
    argparse로 --name, --count 옵션을 받아 인사말 리스트를 반환하세요.

예시:
    - args -> list[str]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 90
TOPIC = "argparse"
TITLE = "CLI 인자 파서"


import argparse


def parse_args_and_build(*args, **kwargs):
    """CLI 인자를 파싱해 문자열 리스트를 만듭니다."""
    argv = list(args[0]) if args else []
    parser = argparse.ArgumentParser()
    parser.add_argument("items", nargs="*")
    parser.add_argument("--upper", action="store_true")
    namespace = parser.parse_args(argv)
    if namespace.upper:
        return [item.upper() for item in namespace.items]
    return namespace.items


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(parse_args_and_build(["--upper", "a", "b"]))


if __name__ == "__main__":
    main()
