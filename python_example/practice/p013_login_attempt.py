"""
Practice 013. 로그인 판정

난이도: beginner
수업 순서: 013
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    아이디/비밀번호가 저장값과 일치하면 True를 반환하세요. 대소문자는 구분합니다.

예시:
    - ("admin", "1234") -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 13
TOPIC = "조건문"
TITLE = "로그인 판정"


def check_login(*args, **kwargs):
    """아이디와 비밀번호가 admin/1234이면 True를 반환합니다."""
    username = str(args[0])
    password = str(args[1])
    return username == "admin" and password == "1234"


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(check_login("admin", "1234"))


if __name__ == "__main__":
    main()
