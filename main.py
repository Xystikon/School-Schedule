import dictionaries
import schedule_pt1
import period_assigning

#HELLOOOOOOO, please check schedule_pt1.py for feedback on your code that you wrote.

def teacher(name, subject=True, grade=True):
	print('Name: ', name)
	if subject and not grade:
		for sbj in dictionaries.teacher_dict[name]:
			print(sbj[0])
	if subject and grade:
		for sbj in dictionaries.teacher_dict[name]:
			print('Class:',sbj[0],'for grade',sbj[1])

def student(name):
	print('Name:', name)
	print('Grade:', dictionaries.student_dict[name]['Grade'])
	print('Classes:', ', '.join(dictionaries.student_dict[name]['Classes']))

# this is a test to see if repl.it can commit to github correctly.