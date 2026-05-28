"""
Practice 096. 미니 프로젝트 성적 리포트

난이도: advanced
수업 순서: 096
학습 주제: project
관련 기본 예제: 종합 실습

문제:
    학생별 점수 입력 후 평균, 등급, 순위를 리포트로 출력하세요.

예시:
    - add_student, build_report

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "advanced"
ORDER = 96
TOPIC = "project"
TITLE = "미니 프로젝트 성적 리포트"


class GradeReport:
    """학생 점수를 추가하고 성적표를 생성합니다."""

    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = list(scores)

    def build_report(self):
        report = []
        for name, scores in sorted(self.students.items()):
            average = sum(scores) / len(scores) if scores else 0.0
            report.append({"name": name, "average": average})
        return report


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    report = GradeReport()
    report.add_student("kim", [90, 80])
    print(report.build_report())


if __name__ == "__main__":
    main()
