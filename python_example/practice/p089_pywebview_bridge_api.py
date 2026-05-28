"""
Practice 089. PyWebView Bridge API

난이도: advanced
수업 순서: 089
학습 주제: pywebview
관련 기본 예제: gui_webview/pywebview_2026

문제:
    프론트엔드에서 호출할 Python API 클래스의 메서드 3개를 설계하세요.

예시:
    - list_files, read_text, save_text

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 89
TOPIC = "pywebview"
TITLE = "PyWebView Bridge API"


from pathlib import Path


class BridgeApi:
    """pywebview에서 호출할 수 있는 파일 API 예시입니다."""

    def __init__(self, root="."):
        self.root = Path(root).resolve()

    def _path(self, name):
        path = (self.root / name).resolve()
        if self.root not in path.parents and path != self.root:
            raise ValueError("허용되지 않은 경로입니다.")
        return path

    def list_files(self):
        return sorted(path.name for path in self.root.iterdir() if path.is_file())

    def read_text(self, name):
        return self._path(name).read_text(encoding="utf-8")

    def save_text(self, name, text):
        path = self._path(name)
        path.write_text(text, encoding="utf-8")
        return True


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    api = BridgeApi(Path(__file__).parent)
    print(isinstance(api.list_files(), list))


if __name__ == "__main__":
    main()
