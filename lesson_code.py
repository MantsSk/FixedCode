class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        for course in self.enrolled_courses:
            grade = self.grades.get(course, "No grade yet")
            print(f"Student: {self.name}, Course: {course.name}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return [course.name for course in self.courses]

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.lessons = []
        self.attendance = {}
        teacher.courses.append(self)  # Add this course to the teacher's course list

    # def __repr__(self):
    #     return self.name

    def add_lesson(self, lesson):
        if isinstance(lesson, Lesson):
            self.lessons.append(lesson)
        else:
            print(f"{lesson} like this doesn't exist")

    def get_lessons(self):
        for lesson in self.lessons:
            print(lesson.get_info())

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            # attendance_status = [f"{date}: {status}" for date, status in attendance_record]
            attendance_status = attendance_record
            print(f"Student: {student.name}, Attendance: {attendance_status}")

class Lesson:
    def __init__(self, topic, date, resources):
        self.topic = topic
        self.date = date
        self.resources = resources

    def get_info(self):
        return f"Lesson: {self.topic}, Date: {self.date}, Resources: {self.resources}"

# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
history_course = Course("History", math_teacher)

alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
alice.enroll(history_course)
bob.enroll(math_course)

lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])

math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)
math_course.add_lesson("ANINASIDNASIDNAS")

print("-----")
math_course.get_lessons()
print("-----")

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
# alice.record_grade(history_course, "A+")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']
