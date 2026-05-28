from pathlib import Path

import webview
from backend.server_flask import CounterApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main():
    server = CounterApiServer(FRONTEND_DIR)
    server.start()

    try:
        webview.create_window(
            "클릭 카운터",
            url=server.base_url,
            width=420,
            height=360,
            resizable=True,
        )
        webview.start()
    finally:
        server.stop()


if __name__ == "__main__":
    main()