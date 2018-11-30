#!/bin/python
# http://hr.gs/fkf 

from datetime import datetime
from datetime import timedelta

# Complete the time_delta function below.
# %z in strptime does not work properly and implement work around.
def new_time(t):
	# creating datetime obj w/o timezone
	l = t.split()
	tz = l[-1]
	t = ' '.join(l[:-1])
	dt = datetime.strptime(t, '%a %d %b %Y %H:%M:%S')
	# timezone operator(+,-)
	tzo = tz[0]
	# timezone hours
	tzh = int(tz[1:3])
	# timezone minutes
	tzm = int(tz[3:5])
	if tzo == '+':
		dt = dt - timedelta(hours=tzh, minutes=tzm)
	else:
		dt = dt + timedelta(hours=tzh, minutes=tzm)
	return dt

def time_delta(t1, t2):
    dt1 = new_time(t1)
    dt2 = new_time(t2)
    l = sorted([dt1, dt2])
    return str(int((l[1] - l[0]).total_seconds()))
    

if __name__ == '__main__':
	t = int(raw_input())
	# input format should be: Sat 02 May 2015 19:54:36
	for t_itr in xrange(t):
		t1 = raw_input()
		t2 = raw_input()
		delta = time_delta(t1, t2)
		print delta




