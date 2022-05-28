# Класс студент
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # 1. Оценка курса преподавателя
    def eval_course(self, lecturer, course, grade):
        if isinstance(self, Student) and course in lecturer.courses_attached \
                and course in self.courses_in_progress \
                and grade in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            print('Ошибка оценки, проверьте вводные данные')

    # 2. Подсчет средней оценки за курсы
    def count_avg(self):
        if self.grades:
            points = []
            for grade in self.grades.values():
                points.append((sum(grade) / len(grade)))
            fin_point = round(sum(points) / len(points), 1)
            return fin_point
        else:
            return "нет курсов/оценок"

    # 3. Вывод информации
    def __str__(self):
        if self.grades:
            res_name = (
                f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка '
                f'за домашние задания: {self.count_avg()}\nКурсы в процессе '
                f'обучения: '
                f'{", ".join(self.courses_in_progress)}\nЗавершенные курсы: '
                f'{", ".join(self.finished_courses)}')
        else:
            res_name = (
                f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка '
                f'за домашние задания: Нет курсов/оценок\nКурсы в процессе '
                f'обучения: '
                f'{", ".join(self.courses_in_progress)}\nЗавершенные курсы:'
                f' {", ".join(self.finished_courses)}')
        return res_name

    # 4. Сравнение
    def __lt__(self, other):
        return self.count_avg() < other.count_avg()


# Класс Ментор
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        if isinstance(self, Lecturer):
            self.courses_grades = {}

    # 1. Оценка студентов
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course\
                in student.courses_in_progress and isinstance(
                self, Reviewer) and grade in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка оценки, проверьте вводные данные")


# Под-Класс Ревьюер
class Reviewer(Mentor):
    def __str__(self):
        res_name = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res_name


# Под-Класс Лектор
class Lecturer(Mentor):

    # 1. Подсчет средней оценки за курсы
    def count_avg(self):
        if self.courses_grades:
            points = []
            for grade in self.courses_grades.values():
                points.append((sum(grade) / len(grade)))
            fin_point = round(sum(points) / len(points), 1)
            return fin_point
        else:
            return "nono"

    # 2. Сравнение
    def __lt__(self, other):
        return self.count_avg() < other.count_avg()

    # 3. Вывод информации
    def __str__(self):
        if self.courses_grades:
            res_name = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя '
                        f'оценка за лекции: {self.count_avg()}')
        else:
            return "Нет оценок"
        return res_name


# Добаляем студентов и их курсы
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Salmon', 'Hinkaly']
best_student.finished_courses += ['Onboarding']

worst_student = Student('Tom', 'Holland', 'your_gender')
worst_student.courses_in_progress += ['Python', 'Salmon', 'Hinkaly']
worst_student.finished_courses += ['Onboarding']

# Добавляем лектора
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Hinkaly']

jack = Lecturer('jack', 'king')
jack.courses_attached += ['Salmon', 'Hinkaly']

# Добавляем ревьюера
paul = Reviewer("Paul", "Maggy")
paul.courses_attached += ['Hinkaly', 'Python', 'Salmon']
paul.rate_hw(best_student, 'Python', 10)
paul.rate_hw(best_student, 'Python', 9)
paul.rate_hw(best_student, 'Salmon', 8)
paul.rate_hw(best_student, 'Hinkaly', 2)
paul.rate_hw(worst_student, 'Python', 2)
paul.rate_hw(worst_student, 'Python', 3)
paul.rate_hw(worst_student, 'Salmon', 7)
paul.rate_hw(worst_student, 'Hinkaly', 2)

sandra = Reviewer("Sandra", "Bullock")
sandra.courses_attached += ['Hinkaly', 'Python', 'Salmon']
sandra.rate_hw(best_student, 'Python', 9)
sandra.rate_hw(best_student, 'Python', 8)
sandra.rate_hw(best_student, 'Salmon', 7)
sandra.rate_hw(best_student, 'Hinkaly', 1)
sandra.rate_hw(worst_student, 'Python', 1)
sandra.rate_hw(worst_student, 'Python', 2)
sandra.rate_hw(worst_student, 'Salmon', 6)
sandra.rate_hw(worst_student, 'Hinkaly', 1)

# Тестируем функции

best_student.eval_course(jack, "Salmon", 5)
best_student.eval_course(cool_mentor, "Python", 2)
worst_student.eval_course(jack, "Salmon", 3)
worst_student.eval_course(cool_mentor, "Hinkaly", 3)
worst_student.eval_course(jack, "Hinkaly", 6)

print()
print(paul)
print()
print(cool_mentor.courses_grades)
print(cool_mentor)
print()
print(jack.courses_grades)
print(jack)

print()
print(best_student.grades)
print(best_student)
print()
print(worst_student.grades)
print(worst_student)

print()
print(jack.count_avg())
print(cool_mentor.count_avg())
print(jack > cool_mentor)
print()

print(best_student.count_avg())
print(worst_student.count_avg())
print(best_student < worst_student)
print()


# Доп функции по средней оценке курса студентов и лекторов
list = [best_student, worst_student]
course_name = "Python"

def count_allstudents(stud_list, course_name):
    list_grades = []
    for el in stud_list:
        if course_name in el.grades.keys():
            list_grades.append(sum(el.grades[course_name]) / len(el.grades[
                                                                     course_name]))
    if list_grades:
        return round(sum(list_grades) / len(list_grades), 1)
    else:
        return "Нет таких курсов"


print(count_allstudents(list, 'Python'))

print()
list = [jack, cool_mentor]
course_name = "Python"


def count_alllecturers(lect_list, course_name):
    list_grades = []
    for el in lect_list:
        if course_name in el.courses_grades.keys():
            list_grades.append(sum(el.courses_grades[course_name]) / len(
                el.courses_grades[course_name]))
    if list_grades:
        return round(sum(list_grades) / len(list_grades), 1)
    else:
        return "Нет таких курсов"

print(count_alllecturers(list, 'Hinkaly'))

