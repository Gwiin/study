"""
Practice 092. 설정 병합

난이도: advanced
수업 순서: 092
학습 주제: dict/json
관련 기본 예제: basic/a25-a100

문제:
    기본 설정, 파일 설정, 환경 설정을 우선순위에 맞게 병합하세요.

예시:
    - env > file > default

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 92
TOPIC = "dict/json"
TITLE = "설정 병합"


import os


def merge_config(*args, **kwargs):
    """default, file, env 설정을 env > file > default 우선순위로 병합합니다."""
    default = dict(args[0]) if args else {}
    file_config = dict(args[1]) if len(args) > 1 else {}
    env_keys = args[2] if len(args) > 2 else file_config.keys() | default.keys()
    result = {**default, **file_config}
    for key in env_keys:
        env_key = str(key).upper()
        if env_key in os.environ:
            result[key] = os.environ[env_key]
    return result


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(merge_config({"mode": "default"}, {"mode": "file"}, ["mode"]))


if __name__ == "__main__":
    main()
