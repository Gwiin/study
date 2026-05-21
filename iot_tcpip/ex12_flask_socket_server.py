# ex12_flask_socket_server.py

# Web server: homepage 같이 사람 대응 (정적 서비스)
# WAS(Web App Server): App 대응 (동적 서비스)

# flask: http 통신, WAS
# custom_thread: tcpip socket


# http 상태코드

import socket, threading
from flask import Flask, render_template_string

app = Flask(__name__)
# 센서 데이터 저장
latest_sensor_data = ""
# ---- TCP 소켓 ----
def start_tcp_server(host, port):
    global latest_sensor_data
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen()
    print(f"TCP 소켓 서버 {host}:{port}에서 대기 중")
    while True:
        client_socket,address = server_socket.accept()
        print(f"연결됨 : {address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data: break
                latest_sensor_data = data.decode('utf-8')
                print(f"수신 데이터: {latest_sensor_data}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


# ---- Flask routing ----
@app.route("/")
def home():
    html = f"""
    <html>
    <head>
        <title>IoT Sensor Dashboard</title>
    </head>
    <body>
        <h1>실시간 센서 값</h1>
        <p>현재 값: {latest_sensor_data}</p>
        <p>[2초 마다 자동 새로 고침 중]</p>
        <script>setTimeout(function(){{location.reload();}}, 2000)</script>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    CLIENT_IP = "0.0.0.0"
    TCP_PORT = 9999
    tcp_thread = threading.Thread(target=start_tcp_server, args=(CLIENT_IP, TCP_PORT))
    tcp_thread.daemon = True
    tcp_thread.start()
    app.run(host='0.0.0.0', port = 5000)







