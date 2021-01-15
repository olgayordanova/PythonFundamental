class Students:

    def __init__(self):
        self.students_dict = {}

    def add_students(self, student_name, grade):
        if student_name not in self.students_dict:
            self.students_dict[student_name] = grade
        else:
            average = (self.students_dict[student_name]+grade)/2
            self.students_dict[student_name] = average

    def __repr__(self):
        sorted_students_dict = dict(sorted(self.students_dict.items(), key=lambda x: x[1], reverse=True))
        result = ''
        for key,  value in sorted_students_dict.items():
            if value >=4.5:
                result += f"{key} -> {value:.2f}" + '\n'
        return result

n=int(input())
students = Students()

for i in range (1, n+1):
    students_name = input()
    grade = float(input())
    students.add_students(students_name,grade)

print(students)