# TCP/IP + Flask 학습 정리

## 저장소 구성

- `ex1` ~ `ex4`: TCP/UDP one-shot, byte 수신, echo server/client
- `ex5` ~ `ex9`: multiprocessing, threading, critical section, asyncio
- `ex10` ~ `ex12`: Pico simulation, multichat, Flask socket/basic route
- `ex13ex13_flask_jinja`: Flask route, Jinja template, static 구조
- `ex20` ~ `ex52`: HTML/CSS 기초, box model, position, transition, flex, media query
- `ex60_total_mysql_flask`: Flask 로그인, 회원가입, 도서 등록, 주문, MySQL 연동
- `img`: HTML image 실습용 이미지

## 네트워크 주소와 port

네트워크 통신은 “어느 장치의 어느 프로그램과 통신할 것인가”를 정하는 일에서 시작함.

- IP address: 장치를 찾는 주소
- port: 한 장치 안에서 프로그램을 구분하는 번호
- protocol: TCP, UDP 같은 통신 규칙

`127.0.0.1`은 자기 자신을 가리키는 loopback 주소임. 같은 컴퓨터에서 server와 client를 동시에 테스트할 때 자주 씀.

## TCP server 흐름

TCP server는 연결을 기다리는 쪽임. 기본 순서는 거의 고정되어 있음.

```text
socket() -> bind() -> listen() -> accept() -> recv()/send() -> close()
```

[ex1_oneshot_server.py](./ex1_oneshot_server.py)의 핵심도 이 흐름임.

```python
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
serv_sock.bind((serv_ip, serv_port))
serv_sock.listen(5)
clnt_sock, clnt_addr = serv_sock.accept()
clnt_sock.send(message.encode('utf-8'))
```

`AF_INET`은 IPv4, `SOCK_STREAM`은 TCP를 의미함. `bind()`는 server 주소를 묶고, `listen()`은 접속 대기 상태로 만들고, `accept()`는 실제 client 연결을 받음.

## TCP client 흐름

TCP client는 server에 접속을 요청하는 쪽임.

```text
socket() -> connect() -> send()/recv() -> close()
```

server가 먼저 실행되어 port를 열고 있어야 client가 접속할 수 있음. 문자열을 보낼 때는 byte로 `encode()`하고, 받은 byte는 `decode()`해야 사람이 읽는 문자열이 됨.

## TCP는 byte stream

TCP는 메시지 단위가 아니라 byte stream임. `recv(1024)`는 최대 1024 byte를 받겠다는 뜻이지, “메시지 하나를 정확히 받는다”는 뜻이 아님.

`ex2_oneshot_client_every1byte.py`처럼 1 byte씩 받아보는 예제는 이 성질을 확인하기 좋음. 실제 protocol을 만들 때는 메시지 길이, 구분자, 고정 크기 header 같은 규칙을 정해야 함.

## UDP

UDP는 연결을 만들지 않고 datagram을 주고받음.

- TCP: 연결 지향, 순서와 재전송 보장
- UDP: 연결 없음, 빠르지만 신뢰성 직접 보장하지 않음

UDP에서는 `sendto()`와 `recvfrom()`을 사용함. `recvfrom()`은 data뿐 아니라 보낸 쪽 주소도 함께 돌려줌.

## echo server

echo server는 받은 메시지를 그대로 다시 보내는 server임. 단순하지만 network program의 반복 송수신 구조를 이해하기 좋음.

```text
client가 보냄 -> server가 받음 -> server가 같은 내용을 돌려줌 -> client가 출력
```

이 구조를 반복문으로 감싸면 한 번만 통신하는 one-shot 예제에서 지속적인 통신 예제로 확장됨.

## process, thread, asyncio

server가 client 한 명을 처리하는 동안 멈춰 있으면 다른 client를 처리할 수 없음. 그래서 동시성 처리가 필요함.

- multiprocessing: process를 여러 개 만들며 메모리 공간이 분리됨.
- threading: 같은 process 안에서 thread를 여러 개 만들며 메모리를 공유함.
- asyncio: event loop가 I/O 대기 시간을 효율적으로 넘김.

thread는 메모리를 공유하므로 list, dict 같은 공유 자료를 동시에 수정할 때 문제가 생길 수 있음. `ex6_1_python_critical_section.py`는 이런 critical section 개념과 연결됨.

## chat server와 broadcast

multichat 예제는 접속한 client 목록을 관리하고, 한 client가 보낸 메시지를 다른 client들에게 전달함.

```text
accept client -> clients list에 저장 -> 메시지 수신 -> 전체 client에 broadcast
```

규모가 커지면 `clients`, `nicknames` 같은 공유 list 접근을 lock으로 보호해야 함. 학습 단계에서는 먼저 “server가 여러 socket을 관리한다”는 흐름을 이해하는 것이 중요함.

## Flask route

Flask는 URL과 Python 함수를 연결함.

```python
@app.route("/")
def index():
    return "hello"
```

browser가 `/`로 HTTP request를 보내면 Flask가 `index()` 함수를 실행하고 response를 돌려줌. socket 예제에서는 직접 byte를 주고받았다면, Flask에서는 HTTP라는 정해진 protocol 위에서 요청과 응답을 처리함.

## Jinja template

Jinja는 Python data를 HTML에 끼워 넣는 template engine임.

```python
return render_template("index.html", title="Home", tasks=items)
```

`templates/`에는 HTML template이 있고, `static/`에는 CSS, JavaScript, image가 들어감. Python 코드가 화면 문자열을 직접 다 만들지 않고 template에 data를 넘기는 구조임.

## HTML 문서 구조

HTML은 화면의 의미 구조를 만듦.

- heading: 제목
- paragraph: 문단
- list: 목록
- table: 표
- form: 사용자 입력
- image/link: 외부 자원 연결

HTML 실습은 tag를 외우는 것보다 “어떤 정보가 어떤 구조로 표현되는가”를 보는 것이 중요함.

## CSS와 box model

CSS는 HTML 요소의 모양과 배치를 제어함. selector로 대상을 고르고 property로 스타일을 정함.

box model은 모든 요소를 content, padding, border, margin으로 보는 관점임. `display`, `position`, `flex` 실습은 요소가 화면에서 어떻게 자리를 차지하는지를 이해하기 위한 단계임.

## transition, transform, animation

`transform`은 요소의 위치, 회전, 크기를 바꿈. `transition`은 상태 변화가 갑자기 일어나지 않고 일정 시간에 걸쳐 변하게 함. `animation`은 keyframe을 기준으로 더 긴 동작을 만듦.

이 개념들은 시각 효과 자체보다 “상태 변화”를 표현하는 방식으로 이해하면 좋음.

## media query와 flex

media query는 화면 크기나 환경에 따라 다른 CSS를 적용함. flex는 한 방향으로 요소를 배치하고 정렬하는 layout 방식임.

반응형 web에서는 고정 pixel 배치보다 container 크기에 따라 자연스럽게 줄바꿈하고 정렬되는 구조가 중요함.

## Flask와 MySQL 연동

`ex60_total_mysql_flask`는 browser, Flask, MySQL이 연결되는 예제임.

```text
Browser -> HTTP request -> Flask route -> MySQL query -> response -> Browser
```

회원가입은 request body를 받아 DB에 저장하고, 로그인은 DB에서 사용자를 찾은 뒤 password hash를 확인함. 주문 기능은 session에 저장된 사용자 정보와 book 정보를 연결함.

## 환경변수와 secret

DB password, Flask secret key 같은 값은 source code에 직접 쓰지 않고 `.env`에서 읽음.

```python
load_dotenv()
app.secret_key = os.getenv("FLASK_SECRET_KEY")
```

이 방식은 보안뿐 아니라 개발 환경과 배포 환경의 설정을 분리하기 위해서도 중요함.
