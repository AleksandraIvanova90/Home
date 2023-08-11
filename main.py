import statistics
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
           
    def average(self):
        list_grades = []
        for course, grades in self.grades.items():
            list_grades += grades
        return statistics.mean(list_grades)
            
    def __str__(self): 
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res      

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average() < other.average()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average() == other.average()
        
    def __ne__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average() != other.average()    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        list_grades = []
        for course, grades in self.grades.items():
            list_grades += grades
        return statistics.mean(list_grades)
        
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average()}'
        return res  

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.average() < other.average()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.average() == other.average()
        
    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.average() != other.average()    
    
class Reviewer(Mentor):        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 
student_1 = Student('Иван', 'Иванов', 'Мужской')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Инженер по тестированию']
student_1.finished_courses += ['Java']

student_2 = Student('Анна', 'Соколова', 'Женский')
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Python']
student_2.finished_courses += ['Java']
 
reviewer_1 = Reviewer('Алексей', 'Нефёдов')
reviewer_1.courses_attached += ['Инженер по тестированию']


reviewer_2 = Reviewer('Олег', 'Смирнов')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['C++']

lecturer_1 = Lecturer('Ольга','Новикова')
lecturer_1.courses_attached += ['Инженер по тестированию']
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Михаил','Петров')
lecturer_2.courses_attached += ['C++']


student_1.rate_lecturer(lecturer_1, 'Инженер по тестированию', 10)
student_1.rate_lecturer(lecturer_1, 'Инженер по тестированию', 9)
student_1.rate_lecturer(lecturer_1, 'Инженер по тестированию', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 9)
reviewer_1.rate_hw(student_1, 'Инженер по тестированию', 9)
reviewer_1.rate_hw(student_1, 'Инженер по тестированию', 8)
reviewer_1.rate_hw(student_1, 'Инженер по тестированию', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'C++', 8)
reviewer_2.rate_hw(student_2, 'C++', 8)
reviewer_2.rate_hw(student_2, 'C++', 9)


print(student_1.average())
print(student_2.average())
print(student_1)
print(student_2)
print(student_1 < student_2)
print(student_1 > student_2)
print(student_1 == student_2)
print(student_1 != student_2)

print(lecturer_1.average())
print(lecturer_2.average())
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)

print(reviewer_1)
print(reviewer_2)

list_student = [student_1, student_2]

def student_rating(list_student, course_name):
    course_grade = []
    for student in list_student:
       if course_name in student.courses_in_progress:
            course_grade += student.grades[course_name]
            
    average_for_all = statistics.mean(course_grade)
    print(f'Cредняя оценка за домашние задания по всем студентам в рамках курса: {course_name} составляет: {average_for_all}')
    
student_rating(list_student, 'C++')
student_rating(list_student, 'Python')
student_rating(list_student, 'Инженер по тестированию')
list_lecturer = [lecturer_1,lecturer_2]
def lecturer_rating(list_lecturer, course_name):
    course_grade = []
    for lecturer in list_lecturer:
       if course_name in lecturer.courses_attached:
           course_grade += lecturer.grades[course_name]
    average_for_all = statistics.mean(course_grade)
    print(f'Cредняя оценка за лекции всех лекторов в рамках курса: {course_name} составляет: {average_for_all}')

lecturer_rating(list_lecturer, 'C++')
lecturer_rating(list_lecturer, 'Python')
lecturer_rating(list_lecturer, 'Инженер по тестированию')