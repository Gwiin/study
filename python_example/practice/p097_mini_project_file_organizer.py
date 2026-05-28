"""
Practice 097. 미니 프로젝트 파일 정리

난이도: advanced
수업 순서: 097
학습 주제: project/pathlib
관련 기본 예제: 종합 실습

문제:
    확장자별 폴더로 파일을 이동하는 계획(plan)을 생성하세요. 실제 이동은 하지 않습니다.

예시:
    - folder -> list[(src,dst)]

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 97
TOPIC = "project/pathlib"
TITLE = "미니 프로젝트 파일 정리"


from pathlib import Path


EXTENSION_FOLDERS = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".docx": "documents",
    ".mp3": "audio",
    ".mp4": "videos",
}


def plan_file_organization(*args, **kwargs):
    """폴더 안 파일을 확장자별 하위 폴더로 옮길 계획을 반환합니다."""
    folder = Path(args[0])
    plan = []
    for path in folder.iterdir():
        if path.is_file():
            target_folder = EXTENSION_FOLDERS.get(path.suffix.lower(), "others")
            plan.append((str(path), str(folder / target_folder / path.name)))
    return plan


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print(plan_file_organization(Path(__file__).parent)[:3])


if __name__ == "__main__":
    main()
