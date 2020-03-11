import dictionaries 



# an example of how it could work -- input is teacher, output is every class they have with someone in it


# takes in a teacher name, a student name, and returns how many times... the teacher has that student? Or how many times the teacher has their classes
def active_hours(teacher_name):
	students = []
	active = 0
	for teacher in dictionaries.teacher_dict: 
		if teacher == teacher_name:  # if the teacher is mentioned in the function call,
			for classes in dictionaries.teacher_dict[teacher]:  # then get every class they teach -- store in 'classes'
				for student in dictionaries.student_dict:  # for every student in existence,
					ls = ['', '']  # create/reset an empty list -- resets for every student called
					for student_classes in range(0,len(dictionaries.student_dict[student]['Classes'])):  # for every class the student has,
						ls[0] = dictionaries.student_dict[student]['Classes'][student_classes]  # then first part of list is a student class,
						ls[1] = dictionaries.student_dict[student]['Grade']  # and the second part is the grade -- this format matches the format the teacher's classes are in
						if ls == classes:  # if they are the same, (ex. ls=['Algebra 1', 9], classes=['Algebra 1', 9])
							students.append(student)  # add the student to the students list
							active += 1  # add 1 to the active count

	return (active, students)  # returns two outputs -- 1: the active hours, 2: the students they have


func = active_hours('Math Teacher')
#print('Total active hours:', func[0], '\nStudents:', ', '.join(func[1]))


