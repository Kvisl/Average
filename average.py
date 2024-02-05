class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        for key, value in self.grades.items():
            return sum(value) / len(value)

    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        end_course = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние: {self._average_grade()}'
                f'\nКурсы в процессе изучения: {in_progress}\nЗавершенные курсы: {end_course}')

    def __gt__(self, other):
        return self._average_grade() > other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        for key, value in self.grades.items():
            return sum(value) / len(value)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'

    def __gt__(self, other):
        return self._average_grade() > other._average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.courses_attached += ['Python', 'Git']
best_student1 = Student('Tom', 'Jerry', 'Cat')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ['Введение в программирование']
best_student1.courses_attached += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer1 = Reviewer('Bill', 'Rum')
cool_reviewer1.courses_attached += ['Python', 'Git']

an_lecturer = Lecturer('Any', 'Random')
an_lecturer.courses_in_progress += ['Python', 'Git']
an_lecturer1 = Lecturer('Eny', 'Dom')
an_lecturer1.courses_in_progress += ['Python', 'Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer1.rate_hw(best_student1,'Python', 9)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 8)


best_student.rate_lecturer(an_lecturer, 'Python', 10)
best_student.rate_lecturer(an_lecturer, 'Python', 8)
best_student.rate_lecturer(an_lecturer, 'Python', 9)
best_student1.rate_lecturer(an_lecturer1, 'Python', 10)
best_student1.rate_lecturer(an_lecturer1, 'Python', 7)
best_student1.rate_lecturer(an_lecturer1, 'Python', 8)


students = [best_student, best_student1]
lecturers = [an_lecturer, an_lecturer1]


def average_grade_stu(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students


def average_grade_lec(lecturers, course):
    all_grades = 0
    all_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += sum(lecturer.grades[course])
            all_lecturers += len(lecturer.grades[course])
            result = all_grades / all_lecturers
            return result


print(f'Reviewer:\n{cool_reviewer}')
print()
print(f'Lecturer:\n{an_lecturer}')
print()
print(f'Student:\n{best_student}')
print()
print('Cравнение лекторов по средней оценке: {}'.format(an_lecturer1._average_grade() > an_lecturer._average_grade()))
print('Cравнение студентов по средней оценке: {}'.format(best_student1._average_grade() > best_student._average_grade()))
print()
print('Средняя оценка всех студентов за курс: {}'.format(average_grade_stu(students, 'Python')))
print('Средняя оценка всех лекторов за курс: {}'.format(average_grade_lec(lecturers, 'Python')))