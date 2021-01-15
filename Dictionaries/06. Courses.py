def sort_by_values_len(dict):
    dict_len= {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = [{item[0]: sorted(dict[item [0]])} for item in sorted_key_list]
    return sorted_dict

class Course:

    def __init__(self, course_name, student_name):
        self.course_name = course_name
        self.student_name = student_name
        self.my_course = {}

    def register(self, course_name, student_name):
        if course_name not in self.my_course:
            self.my_course[course_name] = [student_name]
        else:
            self.my_course[course_name].append ( student_name )

    def output_view(self):
        result = ''
        sorted_courses = sort_by_values_len(self.my_course)
        for el in sorted_courses:
            current_el = dict(el)
            for key, value in current_el.items():
                result += f"{key}: {len ( value )}" + '\n'
                for i in range ( 0, len ( value ) ):
                    current_value = value[i]
                    result += f"-- {current_value}" + '\n'
        return result

course = Course ( '', [] )

while True:
    command = input ()
    if command == 'end':
        break
    course_name, student_name = command.split ( ' : ' )
    course.register ( course_name, student_name )

print ( course )
