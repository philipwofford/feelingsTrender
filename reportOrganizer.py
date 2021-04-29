import datetime

def getDate():
	return datetime.datetime.now()
date_of_analysis = getDate()
print "\nWe generate a gross-to-read date/time object..."
print "\nThe raw date of analysis is: %s\n" % date_of_analysis

def getMonthInEnglish(date):
	month_in_english = ""
	month_as_num = date.month
	# print "The month as a number: %s" % month_as_num 
	if (month_as_num == 1):
		month_in_english = "January"
	elif (month_as_num == 2):
		month_in_english = "February"
	elif (month_as_num == 3):
		month_in_english = "March"
	elif (month_as_num == 4):
		month_in_english = "April"
	elif (month_as_num == 5):
		month_in_english = "May"
	elif (month_as_num == 6):
		month_in_english = "June"
	elif (month_as_num == 7):
		month_in_english = "July"
	elif (month_as_num == 8):
		month_in_english = "August"
	elif (month_as_num == 9):
		month_in_english = "September"
	elif (month_as_num == 10):
		month_in_english = "October"
	elif (month_as_num == 11):
		month_in_english = "November"
	elif (month_as_num == 12):
		month_in_english = "December"
	else: 
		month_in_english = "Oops!"

	return month_in_english

month = getMonthInEnglish(date_of_analysis)
day = date_of_analysis.day
year = date_of_analysis.year

print "\nThen it gets parsed to be more 'human readable'...\n"
print "Performing reports for %s %d, %d..." % (month, day, year)
print "\n (then some magic stuff will happen)"
print " ... and then some new reports will get generated with a nice, human readable date!"
print "\n\nAlright. That's enough for day!\n\n"