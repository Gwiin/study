"""
Practice 076. 설정 singleton

난이도: advanced
수업 순서: 076
학습 주제: singleton
관련 기본 예제: basic/a91

문제:
    ConfigStore가 항상 같은 인스턴스를 반환하도록 구현하세요.

예시:
    - ConfigStore() is ConfigStore() -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 76
TOPIC = "singleton"
TITLE = "설정 singleton"


class ConfigStore:
    """항상 같은 인스턴스를 반환하는 설정 저장소입니다."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.values = {}
        return cls._instance

    def set(self, key, value):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(ConfigStore() is ConfigStore())


if __name__ == "__main__":
    main()
