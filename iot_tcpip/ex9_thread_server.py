# ex9_thread_server.py

import socket, threading, sys

def error_handling(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)

def handle_clnt(clnt_sock, addr):
    print(f"Thread started for client: {addr}")
    try:
        while True:
            data = clnt_sock.recv(1024)
            if not data : break
            clnt_sock.send(data)
    except Exception as e:
        print(f"Error: {addr}, at {e}")
    finally:
        clnt_sock.close()
        print(f"Client {addr} disconnected...")



def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    serv_ip = ''
    serv_port = int(sys.argv[1])
    try:
        serv_sock.bind((serv_ip,serv_port))
    except socket.error:
        error_handling("bind() error")
    if serv_sock.listen(5) == -1:
        error_handling("listen() error")
    print("Multi-threading server started")
    while True:
        try:
            clnt_sock, addr = serv_sock.accept()
            print(f"Connected client IP: {addr[0]}")
            t = threading.Thread(target=handle_clnt, args=(clnt_sock,addr))
            t.start()
        except KeyboardInterrupt:
            break
    serv_sock.close()

if __name__ == "__main__":
    main()
    