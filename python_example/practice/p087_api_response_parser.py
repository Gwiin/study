"""
Practice 087. API 응답 파싱

난이도: advanced
수업 순서: 087
학습 주제: json/api
관련 기본 예제: basic/a100

문제:
    JSON 응답 문자열에서 status와 data를 안전하게 추출하세요.

예시:
    - invalid json -> {"ok": False}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 87
TOPIC = "json/api"
TITLE = "API 응답 파싱"


import json


def parse_api_response(*args, **kwargs):
    """API JSON 문자열을 파싱하고 실패하면 {'ok': False}를 반환합니다."""
    raw = args[0]
    try:
        data = json.loads(raw)
    except (TypeError, json.JSONDecodeError):
        return {"ok": False}
    if isinstance(data, dict):
        return data
    return {"ok": True, "data": data}


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(parse_api_response("not json"))


if __name__ == "__main__":
    main()
