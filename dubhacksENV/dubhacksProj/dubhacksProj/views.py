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
	return render(request, 'major.html', {'page_name': 'Human Centered Design & Engineering','result': row, 'major_description': 'Students in the Human Centered Design & Engineering Bachelor of Science program learn engineering principles rooted in a broad range of disciplines to investigate the interaction of people with technology and technical development.'})

def info(request):
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry WHERE Major LIKE "Informatics"')
	row = cursor.fetchall()
	return render(request, 'major.html', {'page_name': 'Informatics','result': row, 'major_description': 'Informatics students drive innovation as they explore the intersection of technology and human values. Their passion for analyzing and solving problems is reflected in the creativity they bring to the design and creation of information systems, user interfaces, mobile technologies and social media.'})

def cse(request):
	cursor = connection.cursor()
	cursor.execute('SELECT Name, Major, Image FROM dubhacksapp_personentry WHERE Major LIKE "Computer Science & Engineering"')
	row = cursor.fetchall()
	return render(request, 'major.html', {'page_name': 'Computer Science & Engineering','result': row, 'major_description': 'Fusce id fermentum orci. Donec rutrum erat id arcu convallis suscipit. Proin eu neque quis lectus placerat volutpat non ut libero. Nunc laoreet consectetur nunc sed molestie. Sed gravida feugiat magna nec euismod. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla ac nulla nisi. Curabitur pharetra eget sapien vel imperdiet.'})

def about(request):
    return render(request, 'major.html', {'page_name': 'About'})
