"""
Practice 079. 플레이리스트 iterator

난이도: advanced
수업 순서: 079
학습 주제: iterator
관련 기본 예제: basic/a87

문제:
    곡 리스트를 순회하는 Playlist 클래스를 iterator protocol로 구현하세요.

예시:
    - for song in Playlist([...])

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 79
TOPIC = "iterator"
TITLE = "플레이리스트 iterator"


class Playlist:
    """노래 목록을 순회할 수 있는 이터러블입니다."""

    def __init__(self, songs):
        self.songs = list(songs)

    def __iter__(self):
        return iter(self.songs)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(list(Playlist(["a", "b"])))


if __name__ == "__main__":
    main()
