from student import Student

def main():
    students = []

    for i in range(3):
        name = input(f"Enter student {i+1} name: ")
        print("=" * 50)
        student_id = input(f"Enter student {i+1} id: ")
        print("=" * 50)

        homework_score = int(input("Enter homework's score: "))
        print("=" * 50)
        exam_score = int(input("Enter exam's score: "))

        student = Student(name, student_id)
        student.do_homework(homework_score)
        student.take_exam(exam_score)

        students.append(student)

    print("\nList of PASS students")
    for s in students:
        if s.get_result() == "PASS":
            print(f"- {s.name}")
    print("=" * 50)

    print("\nList of FAIL students")
    for s in students:
        if s.get_result() == "FAIL":
            print(f"- {s.name}")
    print("=" * 50)


if __name__ == "__main__":
    main()