"""
Practice 082. SQLite Todo CRUD

난이도: advanced
수업 순서: 082
학습 주제: sqlite3
관련 기본 예제: PyWebView todo_sqlite

문제:
    sqlite3로 todo 테이블을 만들고 추가/완료/목록 함수를 구현하세요.

예시:
    - add, complete, list_open

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 82
TOPIC = "sqlite3"
TITLE = "SQLite Todo CRUD"


import sqlite3


class TodoRepository:
    """SQLite 기반 할 일 저장소입니다."""

    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, done INTEGER DEFAULT 0)"
        )
        self.conn.commit()

    def add(self, title):
        cursor = self.conn.execute("INSERT INTO todos (title, done) VALUES (?, 0)", (title,))
        self.conn.commit()
        return cursor.lastrowid

    def complete(self, todo_id):
        self.conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
        self.conn.commit()

    def list_open(self):
        cursor = self.conn.execute("SELECT id, title FROM todos WHERE done = 0 ORDER BY id")
        return cursor.fetchall()


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    repo = TodoRepository()
    todo_id = repo.add("study")
    print(repo.list_open())
    repo.complete(todo_id)


if __name__ == "__main__":
    main()
