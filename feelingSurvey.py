from sys import argv
import random

this_script, username = argv
REPORT_FILE = "./sampleReports.txt"
FOLLOW_UP_REQUEST_FILE = "./followUpRequests.txt"
THE_NEW_REPORT_FILE = "./myNewReport.txt"

def breaker():

	# compliment1 = "is the best"
	# compliment2 = "is the cat's pajamas"
	# compliment3 = "is doing a great job"
	# compliment4 = "is the bee's knees"
	# compliment5 = "should be proud of the work they do"
	# compliment6 = "does more than people know"

	compliments = ["is the best", "is the cat's pajamas", "is doing a great job", "is the bee's knees", "should be proud of the work they do","does more than people know", "makes the world better"]

	compliment = compliments[random.randint(0, len(compliments) - 1)]

	print ""
	print "_.-*^*-._" * 4, " %s %s! " % (username, compliment), "_.-*^*-._" * 4

def report(file, *data):
	opened_report = open(file, 'a')
	for entry in data:
		opened_report.write("%s \n" % entry)

	opened_report.write("\n")
	opened_report.close()

def analyzer(user, line, start, end):
	breaker()
	if (start > 5):
		print "You started off the day in a good mood!"
	elif (start == 5):
		print "You started off work feeling pretty neutral."
	elif (start < 5):
		print "You started off work not feeling too well..."

	user_mood_trend = "unknown"

	if (end > start):
		print "But it seems your mood improved through the day! That's great, %s!" % user
		user_mood_trend = "positive"

	elif (end == start):
		print "And it seems your mood stayed the same today, %s." % user
		user_mood_trend = "neutral"

	elif (end < start):
		print "Unfortunately, it sounds like you had a pretty rough day. Hopefully tomorrow will be better for you, %s! (especially if it's a day off, amirite?)" % user
		user_mood_trend = "negative"

	# call the report function with the starting user mood, the resulting trend, and the line(s) worked for the report (wip!)
	report(REPORT_FILE, "User Starting Mood Rating: %s" % start, "User Mood Trend: %s" % user_mood_trend, "Line(s) Worked: %s" % line)

	print "\nIn any event, thank you for your effort today, %s. You are truly appreciated, please never forget that." % user

	print "The information you provide can help us make the work you do on the %r line(s) better for you and all the people you serve, in turn." % line

	follow_up_inquiry_results = raw_input("Would you like a follow-up? The only thing included in your request for the follow up will be your username, and your username will not be stored with the results of the survey. Any requests for follow-up would be limited to the information you want to proivde or discuss at the time. (tl;dr want to chat or rant? we can!)")

	report(FOLLOW_UP_REQUEST_FILE, "Respondent: %s" % user, "Follow Up Request Response: %s" % follow_up_inquiry_results)

report(THE_NEW_REPORT_FILE, "Here is some stuff", "I think I should report it", "Not sure how I will use it right now", "but at least I am gathering that data", "that sweet sweet data")
 
breaker()
start_of_work = int(raw_input(""" 
Hi, %s. 

On a scale of 1 - 10, 
with 10 being a great mood,
what was your mood when you started work today?

	Starting Mood Value: """ % username))

breaker()
call_line = raw_input(""" 
Thanks, %s. 

What 'line' did you work today?

	Call Line(s) Worked: """ % username)

breaker()
end_of_work = int(raw_input(""" 
Ok, %s. 

And on a scale of 1 - 10, 
with 10 being a great mood,
what was your mood when you ended work today?

	Ending Mood Value: """ % username))

analyzer(username, call_line, start_of_work, end_of_work)