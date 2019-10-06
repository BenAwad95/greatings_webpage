from flask import Flask,render_template
from datetime import datetime,time




#create the greatings func 

def greatins():
	time_now = datetime.now()
	if 0 <= time_now.hour and 12 > time_now.hour:
		return 'Good morning'
	else:
		return 'Good evening'

#create the time now in form h:m p/am

def time_now():
	time = datetime.now().strftime('%I:%M %p')
	return time

def day_date():
	day_date = datetime.now().strftime('%d-%b-%Y')
	return day_date

def weekday():
	weekday = datetime.now().weekday()
	if weekday == 0:
		weekday = 'Monday'
	elif weekday == 1:
		weekday = 'Tuesday'
	elif weekday == 2:
		weekday = 'Wednesday'
	elif weekday == 3:
		weekday = 'Thursday'
	elif weekday == 4:
		weekday = 'Friday'
	elif weekday == 5:
		weekday = 'Saturday'
	else:
		weekday = 'Sunday'
	return weekday

app = Flask('__name__')




@app.route('/')

def home():
		date = day_date()
		week_day = weekday()
		greatings = '%s Abdullah, What are you doing today?'% greatins()
		time_statement = '%s'% time_now()
		return render_template('home.html',greatings=greatings,time=time_statement,date=date,weekday=week_day)



if __name__ == "__main__":
    app.run(debug=True)

