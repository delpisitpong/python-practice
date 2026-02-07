class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.id = student_id
        self.score = 0

    def do_homework(self, point: int):
        self.score += point
        print("=" * 50)
        print(f"{self.name} did homework {point} points")

    def take_exam(self, point: int):
        self.score += point
        print(f"{self.name} took exam {point} points")
        print("=" * 50)

    def get_result(self) -> str:
        if self.score >= 50:
            return "PASS"
        else:
            return "FAIL"