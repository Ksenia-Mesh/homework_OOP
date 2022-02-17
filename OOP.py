class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_rh(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Eror'

    def __si_grade(self):
        for k in self.grades.values():
            sum = 0
            for val in k:
                sum = sum + val
        return (sum / len(k))

    def __str__(self):
        some_student = f"Name: {self.name}\nSurname: {self.surname}\nAverage mark for lecters:{self.__si_grade()}\nCourses that are taught: { ','.join(self.courses_in_progress)}\nCourses studied: { ','.join(self.finished_courses )} "
        return some_student

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.__si_grade() < other.__si_grade()





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    grades = {}

    def __sr_grade(self):
        for p in self.grades.values():
            sum = 0
            for val in p:
                sum = sum + val
        return (sum / len(p))

    def __str__(self):
        some_lecturer = f'Name: {self.name}\nSurname: {self.surname}\nAverage mark for lecters: {self.__sr_grade()}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.__sr_grade() < other.__sr_grade()


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Name: {self.name}\nSurname: {self.surname} '
        return some_reviewer



best_student = Student('Ruoy', 'Eman', 'your_gender')
next_student = Student('Bob', 'Djovan', 'your_gender')
last_student = Student('Rob', 'Kiol', 'your_gender')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
next_student.courses_in_progress += ['Python']
last_student.courses_in_progress += ['Python']
last_student.courses_in_progress += ['Git']

best_student.finished_courses += ['Introduction to programming']
best_student.finished_courses += ['Git']

cool_mentor = Mentor('Some', 'Buddy')
next_mentor = Mentor('Sim', 'Poi')
last_mentor = Mentor('Ari', 'Hot')

cool_mentor.courses_attached += ['Python']
next_mentor.courses_attached += ['Python']
last_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
next_reviewer = Reviewer('Karl', 'Teddy')
last_reviewer = Reviewer('Mark', 'Lot')

cool_reviewer.courses_attached += ['Python']
next_reviewer.courses_attached += ['Git']
last_reviewer.courses_attached += ['Git']

best_lecturer = Lecturer('Some', 'Buddy')
next_lecturer = Lecturer('Sov', 'Abbi')
last_lecturer = Lecturer('Van', 'Gog')

best_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Python']
last_lecturer.courses_attached += ['Git']



cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

next_reviewer.rate_hw(best_student, 'Python', 10)
next_reviewer.rate_hw(best_student, 'Python', 8)
next_reviewer.rate_hw(best_student, 'Python', 10)

last_reviewer.rate_hw(best_student, 'Python', 10)
last_reviewer.rate_hw(best_student, 'Python', 5)
last_reviewer.rate_hw(best_student, 'Python', 9)




best_student.rate_rh(best_lecturer, 'Python', 10)
best_student.rate_rh(best_lecturer, 'Python', 6)
best_student.rate_rh(best_lecturer, 'Python', 10)

next_student.rate_rh(last_lecturer, 'Python', 10)
next_student.rate_rh(last_lecturer, 'Python', 9)
next_student.rate_rh(last_lecturer, 'Python', 6)

# Средняя оценка за курс по студентам
# student_list = []
def get_avg_grade(student_list, exp):
    sum_hw = []
    # count = 0
    for student in student_list:
        sum_hw.append(student.grades[exp])
        return f'Average rating: {exp} is {sum(sum_hw)/len(sum_hw)}'

# Средняя оценка за курс по лекторам
# lectors_list = []
    def get_avg_grade(lectors_list, exp):
        sum_hw = []
        # count = 0
        for lectors in lectors_list:
            sum_hw.append(lectors.grades[exp])
            return f'Average rating: {exp} is {sum(sum_hw) / len(sum_hw)}'



print(best_student.grades)
print(best_lecturer.grades)
print(cool_reviewer)
print(best_lecturer)
print(best_student)
print(next_lecturer < best_lecturer)
print(last_lecturer > next_lecturer)

