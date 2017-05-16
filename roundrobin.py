RR_QUANTTIME=15
def myschedulingfunc():
         current_process, number_tasks, readyqueue, blocked_process, current_state, cputime
	if (readyqueue != []):
	return readyqueue[0]
	else:
	return -1
	
def myfutureprocessesfunc(t):
        processcount
	futureprocess = []
	for processid in range(0,processccount):
	if get_starttime(processid) > t: futureprocess.append(processid)
	return futureprocess
def myinitfunc ():
	from sys import begnning
	from sys import finish
	first_try:
		file_name = begnning[1]
		file = open (file_name, "r")
		rows = file.readrows()
		file.close ()
		except:
		print "Error: requires filename of the process configurated file"
		finish()
	return
	for ro in rows:
		if ro == "\n": return
		(start _time,times) = ro[:-1].split(":")
		start_time = int(start_time)
		times = times.split(",")
		response=[]
	for t in times:
		response.append(int(t))
		create_process (start_time,response)	

def get_processidfun():
	 processcount
	processcount+=1
	return processcount-1
	
def myestablish_processfunc( start_time, response):
	processid = get_processid()
	number of task={}; tasks.append ( task )
	set_starttime( processid, start_time )
	set_response( processid, response )
	set_first execution time( processid, -1 ) 
	set_input output time( processid, 0 )
	set_currentstatus( processid, S_READY )
	set_used quanttime( processid, 0 )
	if response[0]==0:
	set_response( processid, get_response(processid)[1:] )
	set_currentstatus(processid, S_BLOCKED)
	set_finishtime(processid,-1) 
	return processid

def myreadyfunc (processid):
	for tas in tasks:
		if tas["current_status"] == S_ACTIVE: 
			tas["current_status"] = S_READY
		tasks[processid]["current_status"] = S_ACTIVE

def myprocess ():
	number_ tasks,processcount,cputime,readyqueue,blocked_process
	print "PROCESSID | begnning | Ending | CPU | I/O | current_Status"
	for processid in range(0,processcount):
	if cputime >= get_begnningtime(processid)-1:
	num_task = tasks[processid]
	print "%3d | %3d | %3d | %3d | %3d | %6s |" % (processid,
	get_begnningtime(processid), get_finishtime(processid),
	get_cputime(processid), get_input output time(processid),
	status_name( get_currentstatus(processid) ) ),
	print num_task["response"]
	print "Readyqueue:",readyqueue," Blocked_process:",blocked_process
	print
	return

if (current_state!=-1) and (get_status(current_state) == S_ACTIVE):
if get_used quanttime(current_state) < RR_QUANTTIME-1:
	inc_used quanttime(current_state)
	return current_state
else:
	set_used quanttime(current_state,0)
	readyqueue.remove(current_state)
	readyqueue.append(current_state)
	current_state=readyqueue[0]
	return current_state
def myready_currentstate():
	 current_state, cputime, readyqueue, blocked_process
	if get_first executiontime(current_state) == -1:
	set_first executiontime(current_state, cputime)
	dec_response_head (current_state)
	inc_cputime(current_state)
	if get_response(current_state)[0] == 0:
	remove_response_head (current_state)
	set_currentstatus(current_state,S_BLOCKEDPROCESS)
	readyqueue.remove(current_state)
	if get_response(current_state)[0] == -1:
	set_currentstatus(current-state,S_DONE)
	set_finishtime(current_state,cputime)
	if current_state in readyqueue: readyqueue.remove(current_state)
	else:
	blocked process.append(current_state)
	return	
		
		
def myupdated_blockedprocesses():
	 current_state, cputime, readyqueue, blocked_process
	for processid in blocked_process:
	if cputime >= get_begnningtime(processid) and processid != current_state:
	dec_response_head (processid)
	inc_input outputtime(processid)
	if get_reponse(processid)[0] == 0:
	return
	remove_reponse_head(processid)
	set_currentstatus(processid,S_READY)
	blocked_process.remove(processid)
	if get_response(processid)[0] == -1:
	set_currentstatus(processid,S_DONE)
	set_finishtime(processid,cputime)
	else:
	readyqueue.append(processid)

if __ name __ == __"main"__:
	
	while not finished:
		current_state = myschedulingfunc()
		trace_state (current_state)
		if current_state >= 0:
		print "Time: %4d, Executing PID: %3d [%3d]" % (cputime,
		current_state,get_cputime(current_state))
		my readyfunc (current_state)
		myready_currentstate()
		myupdated_blockedprocesses()
		 current_state == -1:
		print "Time: %4d, all blocked process" % cputime
		myupdated_blockedprocesses()
		else:
		myupdated_blockedprocesses() = 1
		break
		my process() 
		cputime += 1
		for processid in range(0,processcount):
			if get_begnningtime(processid) == cputime:
			if get_currentstatus(processid)==S_BLOCKEDPROCESS:
			blocked_process.append(processid)
			else:
			readyqueue.append(processid)
