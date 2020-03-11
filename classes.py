
students = []
teachers = []


class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes
        students.append(self)

    def teachers(self):
        output = []
        for subject in self.classes:
            for item in class_dict:
                if subject == item:
                    output.append(class_dict[subject][0])
        return output

    def rooms(self):
        output = []
        for teacher in teachers:
            for name in self.teachers():
                if name == teacher.name:
                    output.append(teacher.room)
        return output

    def __repr__(self):
        return 'Grade: ' + str(self.grade) + '\nIn classes: ' + ', '.join(
            sbj for sbj in self.classes)


class Teacher:
    def __init__(self, name, teaches, room):
        self.name = name
        self.teaches = teaches
        self.room = room
        teachers.append(self)

    def students(self):
        output = []
        for student in students:
            for sbj in student.classes:
                if sbj == self.teaches:
                    output.append(student.name)
        return output

    def __repr__(self):
        return 'Teaches \'' + self.teaches + '\' in room ' + str(
            self.room) + '\nStudents: ' + ', '.join(self.students())


Jeff = Student('Jeff', 9, ['Math', 'English'])
Harold = Student('Harold', 10, ['Math', 'Spanish', 'English', 'World History'])
Bob = Student('Bob', 12, ['Arabic', 'World Geo'])
Jaquinious = Student('Jaquinious', 11, ['Biology', 'Human Geo', 'Spanish'])
Darrel = Student('Darrel', 10, ['Chemistry', 'Spanish', 'Latin'])
Abrar = Student('Abrar', 9, ['Spanish', 'World Geo', 'English'])

Math_Teacher = Teacher('Math_Teacher', 'Math', 1)
English_Teacher = Teacher('English_Teacher', 'English', 2)
WH_Teacher = Teacher('WH_Teacher', 'World History', 3)
Bio_Teacher = Teacher('Bio_Teacher', 'Biology', 4)
Spanish_Teacher = Teacher('Spanish_Teacher', 'Spanish', 5)
Arabic_Teacher = Teacher('Arabic_Teacher', 'Arabic', 6)
Chem_Teacher = Teacher('Chem_Teacher', 'Chemistry', 7)
WG_Teacher = Teacher('WG_Teacher', 'World Geo', 8)
HG_Teacher = Teacher('HG_Teacher', 'Human Geo', 9)
Latin_Teacher = Teacher('Latin_Teacher', 'Latin', 10)
