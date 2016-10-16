from django.shortcuts import render

from django.db import connection

def women(request):
    cursor = connection.cursor()
    cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry')
    row = cursor.fetchall()
    return render(request, 'women.html', {'page_name': 'Women', 'result': row})

def hcde(request):
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry WHERE Major LIKE "Human Centered Design & Engineering"')
	row = cursor.fetchall()
	return render(request, 'hcde.html', {'page_name': 'Human Centered Design & Engineering','result': row, 'major_description': 'Students in the Human Centered Design & Engineering Bachelor of Science program learn engineering principles rooted in a broad range of disciplines to investigate the interaction of people with technology and technical development.'})

def info(request):
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry WHERE Major LIKE "Informatics"')
	row = cursor.fetchall()
	return render(request, 'info.html', {'page_name': 'Informatics','result': row, 'major_description': 'Informatics students drive innovation as they explore the intersection of technology and human values. Their passion for analyzing and solving problems is reflected in the creativity they bring to the design and creation of information systems, user interfaces, mobile technologies and social media.'})

def cse(request):
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry WHERE Major LIKE "Computer Science & Engineering"')
	row = cursor.fetchall()
	return render(request, 'cse.html', {'page_name': 'Computer Science & Engineering','result': row, 'major_description': 'Fusce id fermentum orci. Donec rutrum erat id arcu convallis suscipit. Proin eu neque quis lectus placerat volutpat non ut libero. Nunc laoreet consectetur nunc sed molestie. Sed gravida feugiat magna nec euismod. Interdum et malesuada fames ac ante ipsum primis in faucibus.'})

def about(request):
	return render(request, 'major.html', {'page_name': 'About'})


def engineer(request, person_num):
	person_num = int(person_num)
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Response1, Response2, Response3, Response4, Response5, Image FROM dubhacksapp_personentry')
	row = cursor.fetchall()
	name_list = []
	major_list = []
	r1_list = []
	r2_list = []
	r3_list = []
	r4_list = []
	r5_list = []
	img_list = []
	for x in row:
		name_list.append(x[0])
		major_list.append(x[1])
		r1_list.append(x[2])
		r2_list.append(x[3])
		r3_list.append(x[4])
		r4_list.append(x[5])
		r5_list.append(x[6])
		img_list.append(x[7])
	return render(request, 'engineer.html', {'page_name': name_list[person_num], 'portrait_img': img_list[person_num], 'major_name': major_list[person_num], 'answer_one': r1_list[person_num], 'answer_two': r2_list[person_num], 'answer_three': r3_list[person_num]})
