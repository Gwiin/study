# webview_example

`pywebview`로 간단한 데스크톱 창을 띄우는 Python 예제다.

이 프로젝트는 `uv`로 Python 가상환경과 패키지 의존성을 관리하고, Linux에서는 GTK 백엔드를 사용해 `pywebview` 창을 실행한다.

## 1. 프로젝트 폴더로 이동

```bash
cd /home/hrd_1_3/study/python_example/webview_example
```

작업 기준 위치를 프로젝트 루트로 맞춘다. `pyproject.toml`, `uv.lock`, `.venv`가 이 폴더 기준으로 관리된다.

## 2. 시스템 패키지 설치

Ubuntu 22.04 또는 WSL Ubuntu 기준으로 아래 패키지가 필요하다.

```bash
sudo apt-get update
sudo apt-get install -y \
  pkg-config \
  gobject-introspection \
  libgirepository1.0-dev \
  gir1.2-gtk-3.0 \
  gir1.2-webkit2-4.1 \
  libcairo2-dev
```

이 단계가 필요한 이유:

- `pywebview`는 Python 패키지만으로 창을 그리지 않고, 운영체제의 GUI 백엔드를 사용한다.
- Linux에서는 GTK 백엔드를 사용할 수 있고, Python에서 GTK를 쓰려면 `PyGObject`가 필요하다.
- `gir1.2-gtk-3.0`은 GTK 3 정보를 제공한다.
- `gir1.2-webkit2-4.1`은 GTK 안에서 웹 화면을 띄우는 WebKit2GTK 정보를 제공한다.
- `pkg-config`, `libgirepository1.0-dev`, `gobject-introspection`, `libcairo2-dev`는 `PyGObject`와 `pycairo`를 빌드할 때 필요하다.

이 패키지들이 없으면 `uv sync` 중에 `pycairo` 또는 `pygobject` 빌드가 실패하거나, 실행 시 `ModuleNotFoundError: No module named 'gi'`가 발생할 수 있다.

## 3. uv 프로젝트 파일 확인

이 프로젝트의 Python 패키지 설정은 `pyproject.toml`에 적는다.

```toml
[project]
name = "webview-example"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pygobject==3.50.0",
    "pywebview>=6.2.1",
]
```

각 항목의 의미:

- `requires-python = ">=3.13"`은 Python 3.13 이상에서 실행한다는 뜻이다.
- `pywebview>=6.2.1`은 Python 코드에서 `import webview`를 사용할 수 있게 해준다.
- `pygobject==3.50.0`은 Python에서 GTK를 사용할 수 있게 해준다.
- `PyGObject`는 시스템 라이브러리와 함께 빌드되므로, 위의 apt 패키지를 먼저 설치해야 한다.
- Ubuntu 22.04 + Python 3.13 환경에서는 최신 `PyGObject`가 바로 빌드되지 않을 수 있어서 `3.50.0`으로 고정했다.

패키지를 직접 추가할 때는 `pyproject.toml`을 손으로 수정해도 되지만, 보통은 `uv add`를 쓰는 편이 좋다.

```bash
uv add "PyGObject==3.50.0"
uv add pywebview
```

`uv add`를 쓰는 이유:

- `pyproject.toml`에 의존성을 자동으로 추가한다.
- `uv.lock`을 함께 갱신한다.
- 현재 가상환경 `.venv`에도 패키지를 설치한다.

## 4. uv 가상환경 세팅

`pyproject.toml`과 `uv.lock` 기준으로 가상환경을 만든다.

```bash
uv sync
```

이 명령이 하는 일:

- `.venv` 폴더가 없으면 생성한다.
- `pyproject.toml`과 `uv.lock`에 적힌 패키지를 설치한다.
- 이미 설치된 패키지와 잠금 파일 상태를 맞춘다.

설치가 끝나면 프로젝트 내부에 `.venv`가 생긴다.

```bash
ls -a
```

예상되는 주요 파일과 폴더:

```text
.venv
.python-version
README.md
pyproject.toml
uv.lock
timer/
```

## 5. Python 코드 작성

실행 코드는 `timer/main.py`에 작성한다.

```python
import webview


def main():
    webview.create_window("Timer", html="<h1>Hello Webview</h1>")
    webview.start()


if __name__ == "__main__":
    main()
```

코드 설명:

- `import webview`는 `pywebview` 패키지를 가져온다. 패키지 이름은 `pywebview`지만 import 이름은 `webview`다.
- `webview.create_window(...)`는 데스크톱 창 하나를 만든다.
- `"Timer"`는 창 제목이다.
- `html="<h1>Hello Webview</h1>"`는 창 안에 표시할 간단한 HTML이다.
- `webview.start()`는 GUI 이벤트 루프를 시작한다. 이 줄이 있어야 실제 창이 뜬다.
- `if __name__ == "__main__":`는 이 파일을 직접 실행했을 때만 `main()`이 실행되도록 한다.

## 6. 실행

프로젝트 루트에서 실행한다.

```bash
uv run python timer/main.py
```

`uv run`을 쓰는 이유:

- 현재 프로젝트의 `.venv`를 자동으로 사용한다.
- 별도로 `source .venv/bin/activate`를 하지 않아도 된다.
- `pyproject.toml`과 `uv.lock` 기준 환경에서 실행된다.

직접 가상환경 Python을 호출해도 된다.

```bash
/home/hrd_1_3/study/python_example/webview_example/.venv/bin/python \
  /home/hrd_1_3/study/python_example/webview_example/timer/main.py
```

## 7. 설치 확인

`webview` import가 되는지 확인한다.

```bash
uv run python -c "import webview; print(webview.__name__)"
```

정상이라면 아래처럼 출력된다.

```text
webview
```

GTK 백엔드가 준비됐는지 확인한다.

```bash
uv run python -c "import gi; gi.require_version('Gtk', '3.0'); import webview.platforms.gtk"
```

아무 에러 없이 끝나면 GTK 백엔드 import는 성공한 것이다.

## 8. 자주 나는 에러

### `ModuleNotFoundError: No module named 'webveiw'`

`webview` 철자를 잘못 쓴 경우다.

잘못된 코드:

```python
import webveiw
```

올바른 코드:

```python
import webview
```

### `ModuleNotFoundError: No module named 'gi'`

`PyGObject`가 설치되지 않았거나 GTK 관련 시스템 패키지가 부족한 경우다.

해결 순서:

```bash
sudo apt-get update
sudo apt-get install -y \
  pkg-config \
  gobject-introspection \
  libgirepository1.0-dev \
  gir1.2-gtk-3.0 \
  gir1.2-webkit2-4.1 \
  libcairo2-dev

uv sync
```

### `You must have either QT or GTK with Python extensions installed`

`pywebview`는 설치됐지만 GUI 백엔드가 준비되지 않은 상태다.

이 예제는 GTK를 사용하므로 아래를 확인한다.

```bash
uv run python -c "import gi; gi.require_version('Gtk', '3.0'); import webview.platforms.gtk"
```

실패하면 2번의 시스템 패키지 설치부터 다시 확인한다.

## 9. 전체 순서 요약

처음부터 구성할 때는 아래 순서대로 진행한다.

```bash
cd /home/hrd_1_3/study/python_example/webview_example

sudo apt-get update
sudo apt-get install -y \
  pkg-config \
  gobject-introspection \
  libgirepository1.0-dev \
  gir1.2-gtk-3.0 \
  gir1.2-webkit2-4.1 \
  libcairo2-dev

uv sync
uv run python -c "import webview; print(webview.__name__)"
uv run python -c "import gi; gi.require_version('Gtk', '3.0'); import webview.platforms.gtk"
uv run python timer/main.py
```
