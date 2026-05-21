# Python

## 2026-05-21

- conda 사용하는 이유 : 가상환경을 사용하기 위해서
> 1. dependency(의존성)<br>
`.venv/` => 프로젝트 마다 라이브러리 관리<br>
.venv 를 만들어도 root 의 바이너리를 공유하지만<br>
conda로 가상환경을 만들면 가상환경내에 바이너리를 만들어서 사용한다

> ! conda로 가상환경을 만들어도 커널은 공유한다 커널까지 가상화를 위해서 WSL 같은것을 사용한다

> 커널 상위의 가상환경 => VM머신


```
C
main() 필수 
컴파일 언어
코드 완성이 전제
전처리 -> 어셈블리 -> 바이너리(기계어)
```

```
Python
1번 라인
built-in varialbe 이 있다
인더액티브셀로 실행
인터프리터(C언어 프로그램) 언어
```

[C로 만든 인터프리터](https://github.com/Gwiin/study/blob/main/basic/interpreter.c)
