# helLLLOOOOOO, i just am doing all the boring stuff, I'm giving the students and teachers more realistic classes etc

# periods and classes probably don't need to be lists, but can just be integers later on. Maybe having them be strings will be too much unnecessary work.

periods = [
    'FirstPrd', 'SecondPrd', 'ThirdPrd', 'FourthPrd', 'FifthPrd', 'SixthPrd',
    'SeventhPrd', 'EighthPrd'
]

rooms = [
    'Room1', 'Room2', 'Room3', 'Room4', 'Room5', 'Room6', 'Room7', 'Room8',
    'Room9', 'Room10'
]

# every teacher has a list of: class and grade

# im wondering: how about the teacher's inputs would just be what classes they want to take (ex. spanish 1-4), and then which grades they want to teach in (9-12) and the program figures out which grades need teaching.

teacher_dict = {
	'Math Teacher': [
		['Algebra 1', 8], ['Algebra 1', 9], ['Algebra 2', 10], ['Algebra 2', 11], ['Geometry', 9], 	['Geometry', 10], ['Geometry', 11]],
	'English Teacher': [
		['English 1', 9], ['English 1', 10], ['English 2', 9], ['English 2', 10], ['English 3', 10], ['English 3', 11]],
	'Social Studies Teacher': [
		['World History 1', 9], ['World History 1', 10], ['World History 2', 9], ['World History 2', 10], ['US History 1', 11], ['US History 1', 12]],
	'Science Teacher': [
		['Biology', 9], ['Biology', 10], ['Chemistry', 10], ['Chemistry', 11], ['Physics', 11], ['Physics', 12]],
	'Spanish Teacher': [
		['Spanish 1', 9], ['Spanish 1', 10], ['Spanish 2', 9], ['Spanish 2', 10], ['Spanish 3', 10], ['Spanish 3', 11], ['Spanish 4', 11], ['Spanish 4', 12]],
	'Arabic Teacher': [
		['Arabic 1', 9], ['Arabic 1', 10], ['Arabic 2', 9], ['Arabic 2', 10], ['Arabic 3', 10], ['Arabic 3', 11], ['Arabic 4', 11], ['Arabic 4', 12]],
	'Latin Teacher': [
		['Latin 1', 9], ['Latin 1', 10], ['Latin 2', 9], ['Latin 2', 10], ['Latin 3', 10], ['Latin 3', 11], ['Latin 4', 11], ['Latin 4', 12]]
}

# every student has math, english, social studies, science, PE, language, elective

student_dict = {
	'Jeff': {
		'Grade': 9,
		'Classes': ['Algebra 1', 'English 2', 'World History 1', 'Biology', 'PE 9', 'Spanish 1', 'Orchestra'],
    'OrgClasses': []
  },
	'Harold': {
		'Grade': 10,
		'Classes': ['Algebra 2', 'English 1', 'World History 2', 'Chemistry', 'PE 10', 'Latin 2', 'Orchestra'],
    'OrgClasses': []
  },
	'Bob': {
		'Grade': 9,
		'Classes': ['Geometry', 'English 1', 'World History 1', 'Biology', 'PE 9', 'Arabic 1', 'Orchestra'],
    'OrgClasses': []
	},
	'Jaquinious': {
		'Grade': 11,
		'Classes': ['Pre-calculus', 'English 3', 'US History 1', 'Physics', 'None', 'Spanish 3', 'Orchestra'],
    'OrgClasses': []
	},
	'Darrel': {
		'Grade': 9,
		'Classes': ['Algebra 1', 'English 2', 'World History 1', 'Biology', 'PE 9', 'Spanish 1', 'Orchestra'],
    'OrgClasses': []
	},
	'Harry': {
		'Grade': 10,
		'Classes': ['Algebra 2', 'English 1', 'World History 2', 'Chemistry', 'PE 10', 'Latin 2', 'Orchestra'],
    'OrgClasses': []
	},
	'Alfred': {
		'Grade': 9,
		'Classes': ['Geometry', 'English 1', 'World History 2', 'Biology', 'PE 9', 'Arabic 1', 'Orchestra'],
    'OrgClasses': []
	},
	'Connor': {
		'Grade': 12,
		'Classes': ['Calculus 1', 'English 4', 'US History 1', 'Physics', 'None', 'Spanish 4', 'Orchestra'],
    'OrgClasses': []
  },
	'Kevin': {
		'Grade': 10,
		'Classes': ['Algebra 2', 'English 1', 'World History 2', 'Chemistry', 'PE 10', 'Latin 2', 'Orchestra'],
    'OrgClasses': []
  },
	'Michael': {
		'Grade': 9,
		'Classes': ['Algebra 1', 'English 1', 'World History 1', 'Biology', 'PE 9', 'Spanish 1', 'Orchestra'],
    'OrgClasses': []
  },
}

