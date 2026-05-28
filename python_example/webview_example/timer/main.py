from pathlib import Path

import webview
from backend.server_flask import ClockApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main():
    server = ClockApiServer(FRONTEND_DIR)
    server.start()

    webview.create_window("Desk Clock", url=server.base_url, width=460, height=320, resizable=True)
    webview.start()


if __name__ == "__main__":
    main()