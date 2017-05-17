RR_QUANTTIME=25
def myschedulingfunc():
         current_process=0
		  number_tasks={}
		  readyqueue=[]
		  blocked_process={}
		   current_state=0
		   cputime=0
	if (readyqueue != []):
	return readyqueue[0]
	else:
	return -1
	
def myfutureprocessesfunc(t):
        processcount=0
	futureprocess = []
	for processid in range(0,processccount):
	if get_starttime(processid) > t: 
	futureprocess.append(processid)
	return futureprocess

def mystartingfunc ():
	      begnning=1
	first_try:
		file_name = begnning[1]
		file = open (file_name, "r")
		rows = file.readrows()
		file.close ()
		except:
		print ("Error in this file")
		finish()
	return

def get_processidfun():
	 processcount=0
	processcount+=1
	return processcount-1
	
def myestablish_processfunc( start_time, response):
	processid = get_processid()
	number of task={}; tasks.append ( task )
	set_starttime( processid, start_time )
	set_first execution time( processid, -1 ) 
	set_input output time( processid, 0 )
	set_currentstatus( processid, READY)
	set_used quanttime( processid, 0 )
	set_currentstatus(processid, BLOCKED)
	set_finishtime(processid,-1) 
	return processid

def myreadyfunc (processid):
	for tas in tasks:
		if tas["current_status"] == S_ACTIVE: 
			tas["current_status"] = S_READY
		tasks[processid]["current_status"] = S_ACTIVE

def myprocess ():
	number_ tasks={}
	processcount=0
	cputime=0
	readyqueue=[]
	current_state=-1
	blocked_process={}
	print ("PROCESSID | begnning | Ending | CPU | I/O | current_Status")
	for processid in range(0,processcount):
	if cputime >= get_begnningtime(processid)-1:
	num_task = tasks[processid]
	print ("processid, get_begnningtime(processid), get_finishtime(processid),
	get_cputime(processid), get_input output time(processid),
	status_name( get_currentstatus(processid) ) ),
	print ("num_task[]")
	print( "Readyqueue:",readyqueue," Blocked_process:",blocked_process)
	return

if (current_state!=-1) and (get_status(current_state) == S_ACTIVE):
if get_used quanttime(current_state) < RR_QUANTTIME-1:
	inc_used quanttime(current_state)
	return current_state

def myready_currentstate():
	 current_state=-1
	 cputime=0
	  readyqueue=[]
	  blocked_process={}
	if get_first executiontime(current_state) == -1:
	set_first executiontime(current_state, cputime)
	inc_cputime(current_state)
	set_currentstatus(current_state,BLOCKEDPROCESS)
	readyqueue.remove(current_state)
	set_currentstatus(current_state)
	set_finishtime(current_state,cputime)
	if current_state in readyqueue: 
	readyqueue.remove(current_state)
	return	
		
if __ name __ == __"main"__:

		current_state = myschedulingfunc()
		trace_state (current_state)
		if current_state >= 0:
		print ("Time,Executing PID ":cputime,current_state,get_cputime(current_state))
		my readyfunc (current_state)
		myready_currentstate()
		 current_state == -1:
		print ("Time and all blocked process" % cputime)
		break
		my process() 
		cputime += 1
		for processid in range(0,processcount):
			if get_begnningtime(processid) == cputime:
			if get_currentstatus(processid)==BLOCKEDPROCESS:
			blocked_process.append(processid)
			else:
			readyqueue.append(processid)
