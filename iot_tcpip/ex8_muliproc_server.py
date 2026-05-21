# ex8_muliproc_server.py
# ex4_echo_client.py 그대로 사용

import socket, multiprocessing, os, sys

def error_handling(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)

def handle_client(clnt_sock, addr):
    print(f"Chils process handling  client: {addr}")
    try:
        while True:
            data = clnt_sock.recv(1024)
            if not data:
                break
            clnt_sock.send(data)

    finally:
        clnt_sock.close()
        print(f"client {addr} disconnected...")
    
def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if serv_sock.fileno() == 1:
        error_handling("socket() error")
    
    serv_ip = ''
    serv_port = int(sys.argv[1])

    try:
        serv_sock.bind((serv_ip,serv_port))
    except socket.error:
        error_handling("bind() error")
    serv_sock.settimeout(1.0) # 1초마다 accept에서 빠져나와 신호 확인
    serv_sock.listen(5)
    print("Multi-process server started!")

    while True:
        try:
            try:
                clnt_sock, clnt_addr = serv_sock.accept()
                print("new client connected")
            except socket.timeout: # 타임 아웃 발생 시 다시 루프로 돌아가 신호 체크
                continue
        except KeyboardInterrupt:
            break
        except Exception:
            continue
        #fork()
        p = multiprocessing.Process(target=handle_client, args=(clnt_sock, clnt_addr))

        p.start()
        clnt_sock.close()
    serv_sock.close()

if __name__ == "__main__":
    main()