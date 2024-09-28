from django.shortcuts import render
import datetime
import random

def result_view(request):
	msg_list = [
		'The golden days ahead',
		'Better to sleep more time even in class',
		'Tomorrow will be the best day in your life',
		"You'll get job very soon"
	]
	names_list = ['Sunny', 'Radha', 'Lotus', 'Katrina', 'Karishma', 'Deepa', 'Santan']
	time = datetime.datetime.now()
	h = int(time.strftime('%H'))
	if h <= 12:
		s = 'Good Morning'
	elif h < 16:
		s = 'Good Afternoon'
	elif h < 21:
		s = 'Good Evening'
	else:
		s = 'Good Night'
	msg = random.choice(msg_list)
	name = random.choice(names_list)
	my_dict = {'time':time, 'name':name, 'msg':msg, 'wish':s}
	return render(request,'testapp/astrology.html',my_dict)