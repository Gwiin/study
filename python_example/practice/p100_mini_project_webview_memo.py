"""
Practice 100. 미니 프로젝트 WebView 메모 API

난이도: advanced
수업 순서: 100
학습 주제: project/pywebview
관련 기본 예제: gui_webview/pywebview_2026

문제:
    PyWebView 프론트엔드와 연결할 메모 저장/목록/삭제 API 클래스를 설계하세요.

예시:
    - create, list_all, delete

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 100
TOPIC = "project/pywebview"
TITLE = "미니 프로젝트 WebView 메모 API"


from pathlib import Path


class MemoApi:
    """메모를 파일로 생성, 조회, 삭제하는 API입니다."""

    def __init__(self, root="memos"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def create(self, title, content):
        filename = f"{title}.txt"
        path = self.root / filename
        path.write_text(content, encoding="utf-8")
        return filename

    def list_all(self):
        return sorted(path.stem for path in self.root.glob("*.txt"))

    def read(self, title):
        return (self.root / f"{title}.txt").read_text(encoding="utf-8")

    def delete(self, title):
        path = self.root / f"{title}.txt"
        if path.exists():
            path.unlink()
            return True
        return False


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    api = MemoApi(Path(__file__).with_suffix(".memos"))
    api.create("today", "study")
    print(api.list_all())
    api.delete("today")


if __name__ == "__main__":
    main()
