# ex1_oneshot_server.py

# 서버 실행 : python ~server.py 8000(port)
# Client 실행 : python ~client.py 127.0.0.1 8000

import socket
import sys
    

def main():

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)

    serv_ip = ''
    serv_port = int(sys.argv[1])
    

    # step1 : socket
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    try:
        serv_sock.bind((serv_ip,serv_port))
        serv_sock.listen(5)
        print("NOW I am listening...!")

        clnt_sock, clnt_addr = serv_sock.accept()
        print(f"Connected from: {clnt_addr}")

        message = "hello this is server speaking"
        clnt_sock.send(message.encode('utf-8'))
        clnt_sock.close()

    except Exception as e:
        print(f"error: {e}")

    finally:
        serv_sock.close()

# C언어 : ifndef
if __name__ == "__main__":
    main()
