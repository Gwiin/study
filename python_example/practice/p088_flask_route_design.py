"""
Practice 088. Flask 라우트 설계

난이도: advanced
수업 순서: 088
학습 주제: flask
관련 기본 예제: web/flask_test

문제:
    간단한 Flask 앱에서 /health와 /api/sum 라우트를 구성하세요.

예시:
    - create_app() returns Flask app

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 88
TOPIC = "flask"
TITLE = "Flask 라우트 설계"


def create_app(*args, **kwargs):
    """간단한 Flask 앱을 생성합니다."""
    try:
        from flask import Flask, jsonify
    except ImportError as error:
        raise ImportError("flask가 필요합니다.") from error

    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify({"message": "hello"})

    @app.get("/health")
    def health():
        return jsonify({"ok": True})

    return app


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    try:
        app = create_app()
        print(app.name)
    except ImportError as error:
        print(error)


if __name__ == "__main__":
    main()
