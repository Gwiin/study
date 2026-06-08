from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DEMO_DIR = BASE_DIR / "demo_files"


class FileListApi:
    def __init__(self):
        pass

    def list_files(self):
        files = []
        for path in sorted(DEMO_DIR.iterdir()):
            if path.is_file():
                files.append({"name": path.name,
                              "suffix": path.suffix or "(none)",
                              "size": path.stat().st_size
                              })
        return files


def main():
    webview.create_window(
        "파일 정보 확인",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=FileListApi(),
        width=520,
        height=420,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()