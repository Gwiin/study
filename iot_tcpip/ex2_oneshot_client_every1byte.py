# ex2_oneshot_client_every1byte.py


import socket, sys

def error_handling(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <IP> <port>")
        sys.exit(1)
    # step 1: socket()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    if sock.fileno() == -1:
        error_handling("socket() error")

    # step 2: 주소 설정
    serv_ip = sys.argv[1]
    serv_port = int(sys.argv[2])

    # step 3: connect()
    try:
        sock.connect((serv_ip,serv_port))
    except:
        error_handling("socket connect() error")

    # step 4: read() - 1 Byte 씩 읽는 것으로 수정
    # try:
    #     message_from_server = sock.recv(30)
    #     if not message_from_server:
    #         error_handling("no contents error")
    #     print(f"Message from server: {message_from_server.decode('utf-8')}")
    # except socket.error:
    #     error_handling("read() error")

    message_buffer = bytearray(30) # 배열
    str_len = 0
    idx = 0
    while True:
        read_byte = sock.recv(1) # 1byte 씩 읽기
        if not read_byte: # 읽은 것이 없으면 루프 탈출
            break
        message_buffer[idx] = read_byte[0]
        idx+=1
        str_len+=1
    received_message = message_buffer[:idx].decode('utf-8')
    print(f"Function read call count: {str_len}")
    print(f"Message from server: {received_message}")


    sock.close()
    

if __name__ == "__main__":
    main()
