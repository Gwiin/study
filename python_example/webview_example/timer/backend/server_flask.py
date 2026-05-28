from flask import Flask
from threading import Thread
from werkzeug.serving import make_server
import socket
from datetime import datetime

WEEKDAYS = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]

def getClockpayload():
    now = datetime.now()
    return {"time": now.strftime("%H:%M:%S"), "date": f"{now.year}년{now.month}월{now.day}일{WEEKDAYS[now.weekday()]}"}

def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1",0))
        return int(sock.getsockname()[1])

class ClockApiServer:
    def  __init__(self, frontend_dir):
        self.port = getFreePort()
        self.app = Flask(__name__, static_folder=str(frontend_dir), static_url_path="")
        
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)

        self.app.add_url_rule("/","index", lambda: self.app.send_static_file("index.html"))
        self.app.add_url_rule("/api/clock","clock",lambda: getClockpayload())
        # self.base_url = "http:127.0.0.1:8888"

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        self._thread.start()
