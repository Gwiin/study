# ex1_oneshot_server.py

# 서버 실행 : python ~server.py 8000(port)
# Client 실행 : python ~client.py 127.0.0.1 8000

import socket
import sys

def error_handling(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)
    
    

def main():

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    # step1 : socket
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    if serv_sock.fileno()==-1:
        error_handling("socket() error")

    # step2 : 주소 설정
    serv_ip = '' # 172.30.1.8 이렇게 넣어도 되고, 비워두면 adress any
    serv_port = int(sys.argv[1]) # ex 8000

    # step3 : bind()
    try:
        serv_sock.bind((serv_ip,serv_port))
    except socket.error:
        error_handling("bind() error")

    # step4 : listen()
    if serv_sock.listen(5) == -1:
        error_handling("listen() error")

    # step5 : accept()
    try:
        clnt_sock, clnt_addr = serv_sock.accept()
    except socket.error:
        error_handling("accept() error")

    # step6 : c코드 : write() - python send()에 대응
    message = "hello this is server speaking"
    clnt_sock.send(message.encode('utf-8'))
    clnt_sock.close()
    serv_sock.close()



# C언어 : ifndef
if __name__ == "__main__":
    main()
