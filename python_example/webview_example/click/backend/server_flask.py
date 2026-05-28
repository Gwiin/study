import json
import queue
import socket
from datetime import datetime
from pathlib import Path
from threading import Lock, Thread
from urllib import error, request

from flask import Flask, Response, send_from_directory
from werkzeug.serving import make_server

FORT_NUMBER = 11722


class CounterApiServer:
    def __init__(self, frontend_dir):
        self.frontend_dir = Path(frontend_dir).resolve()
        self.port = FORT_NUMBER
        self._count = 0
        self._lock = Lock()
        self._event_clients = []
        self.app = Flask(
            __name__,
            static_folder=str(self.frontend_dir),
            static_url_path="",
        )
        self._owns_server = False
        self._server = None
        self._thread: Thread | None = None
        self.app.add_url_rule("/", "index", self._serve_index)
        self.app.add_url_rule("/api/counter", "counter", self._counter_payload)
        self.app.add_url_rule("/api/counter/increase", "increase", self._increase_payload, methods=["Post"])
        self.app.add_url_rule("/api/counter/decrease", "decrease", self._decrease_payload, methods=["Post"])
        self.app.add_url_rule("/api/counter/events", "events", self._stream_counter_events)

    def _serve_index(self):
        return send_from_directory(self.frontend_dir, "index.html")

    def _counter_payload(self):
        with self._lock:
            return {"count": self._count}

    def _broadcast_counter(self, payload):
        for client_queue in list(self._event_clients):
            client_queue.put(payload)

    def _increase_payload(self):
        with self._lock:
            self._count += 1
            payload = {"count": self._count}
        self._broadcast_counter(payload)
        return payload

    def _decrease_payload(self):
        with self._lock:
            self._count -= 1
            payload = {"count": self._count}
        self._broadcast_counter(payload)
        return payload

    def _stream_counter_events(self):
        client_queue = queue.Queue()
        with self._lock:
            self._event_clients.append(client_queue)
            client_queue.put({"count": self._count})

        def eventStream():
            try:
                while True:
                    payload = client_queue.get()
                    yield f"data: {json.dumps(payload)}\n\n"
            finally:
                with self._lock:
                    if client_queue in self._event_clients:
                        self._event_clients.remove(client_queue)
        return Response(eventStream(), mimetype="text/event-stream")

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def _isServerReady(self):
        try:
            with request.urlopen(f"{self.base_url}/api/counter", timeout=1) as resp:
                return resp.status == 200
        except (OSError, error.URLError):
            return False

    def start(self):
        if self._isServerReady():
            print("서버가 존재해서 리턴한다.")
            return
        print("서버가 존재 하지 않는다.")
        try:
            self._server = make_server("127.0.0.1", self.port, self.app, threaded=True)
        except OSError as exc:
            if exc.errno in {10048, 98} and self._isServerReady():
                return
            raise
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        self._owns_server = True

    def stop(self):
        if not self._owns_server or self._server is None or self._thread is None:
            return
        self._server.shutdown()
        self._thread.join(timeout=1)