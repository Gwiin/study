# study0309
학습저장소

---

## 2026-03-09

    - 구글 슬라이드 자기소개
    - wsl 설치
    - vscode, git 설치
    - os (리눅스 wsl 사용)

    - Ubuntu install
    '''
    wsl --install -d Ubuntu-22.04
    wsl --set-default-version 2
    wsl --set-version Ubuntu-22.04 2
    wsl -l -v
    '''

    - 터미널에서 유저 정보 입력
    '''
    git config --global user.email freshmea@gmail.com
    git config --global user.name freshmea
    '''


    1. hello.c 작성
        '#' -> 전처리 지시자
        'main' 함수 -> 엔트리 포인트
        함수의 리턴값의 타입과 함수이름앞의 타입은 같아야함

    2. literal.c 작성
        |   |   |
        |---|---|
        | '%d' | 10진수로 표현 |
        | '0%o' | 8진수로 표현 |
        | '0x%x' | 16진수로 표현 |
        | '%c' | 문자 |
        | '%s' | 문자열(포인터) |

        %d -> 10진수로 표현
        0%o -> 8진수로 표현
        0x%x -> 16진수로 표현
        %c -> 문자
        문자 -> %d / 숫자 -> %c => 아스키코드에 해당하는 값으로 
        %s -> 문자열 (C에서는 문자열을 포인터로)

    3. limit.c 작성
        최대 비트수 확인 ( '<limits.h>' )
       ' #define END_HELLO "end of file\n"' => 'END_HELLO'를 '"end of file\n"' 로 치환


    [실습폴더](./c_example/)


---


