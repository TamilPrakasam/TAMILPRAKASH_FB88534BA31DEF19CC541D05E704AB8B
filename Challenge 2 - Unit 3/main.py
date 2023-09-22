class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, cgpa={self.cgpa})"


def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Example usage
students = [
    Student("Alice", "A101", 3.8),
    Student("Bob", "B102", 3.6),
    Student("Charlie", "C103", 3.9),
    Student("David", "D104", 3.7)
]

sorted_students = sort_students(students)

# Print sorted students
for student in sorted_students:
    print(student)
