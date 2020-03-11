class SS:

  # input is a student name, output is the classes the student is in
    def get_classes(std):
        for student in student_dict:
            if student == std:
                return student_dict[std]

    # input is a class, output is the teacher of that class
    def get_teacher(std_class):
        for sbj in class_dict: 
            if sbj == std_class:
                return class_dict[sbj][0]

    # input is the teacher, output is the subject they teach
    def get_teaches(tchr):
        for sbj in class_dict:
            if class_dict[sbj][0] == tchr:
                return sbj

    # input is the class, output is every student in that class
    def get_students(tchr_class):
        output = []
        for std in student_dict:
            for sbj in student_dict[std]:
                if sbj == tchr_class:
                    output.append(std)
        return output

    # input is a student name, to every class they are in, to every teacher of every class
    def students_to_classes(std):
        print('Student:', std)
        for sbj in SS.get_classes(std):
            print('Subject',
                  SS.get_classes(std).index(sbj) + 1, ':', sbj, '    Teacher:',
                  SS.get_teacher(sbj))

    # input is a teacher name, to the subject they teach, to every student in the class
    def teachers_to_students(tchr):
        print('Teacher:', tchr)
        print('Teaches:', SS.get_teaches(tchr))
        for std in SS.get_students(SS.get_teaches(tchr)):
            print('Student',
                  SS.get_students(SS.get_teaches(tchr)).index(std) + 1, ':',
                  std)

    # input is a student name, output is every room and class they go to
    def students_to_rooms(std):
        print('Student:', std)
        for subject in SS.get_classes(std):
            for sbj in class_dict:
                if subject == sbj:
                    print('Class:', sbj, ', Room:', (class_dict[sbj][1])[-1])

    # input is a class, output is every student in such class
    def classes_to_students(s_cls):
        print('Class:', s_cls)
        for std in SS.get_students(s_cls):
            print('Student', SS.get_students(s_cls).index(std) + 1, ':', std)


periods = [
    'FirstPrd', 'SecondPrd', 'ThirdPrd', 'FourthPrd', 'FifthPrd', 'SixthPrd',
    'SeventhPrd', 'EighthPrd'
]
rooms = [
    'Room1', 'Room2', 'Room3', 'Room4', 'Room5', 'Room6', 'Room7', 'Room8',
    'Room9', 'Room10'
]
class_dict = {
    'Math': ['Math_Teacher', 'Room1'],
    'English': ['English_Teacher', 'Room2'],
    'World History': ['WH_Teacher', 'Room3'],
    'Biology': ['Bio_Teacher', 'Room4'],
    'Spanish': ['Spanish_Teacher', 'Room5'],
    'Arabic': ['Arabic_Teacher', 'Room6'],
    'Chemistry': ['Chem_Teacher', 'Room7'],
    'World Geo': ['WG_Teacher', 'Room8'],
    'Human Geo': ['Humangeo_Teacher', 'Room9'],
    'Latin': ['Latin_Teacher', 'Room10']
}
student_dict = {
    'Jeff': ['Math', 'English'],
    'Harold': ['Math', 'Spanish', 'English', 'World History'],
    'Bob': ['Arabic', 'World Geo'],
    'Jaquinious': ['Biology', 'Human Geo', 'Spanish'],
    'Darrel': ['Chemistry', 'Spanish', 'Latin']
}

