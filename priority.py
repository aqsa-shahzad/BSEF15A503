#!usr/bin/env python


total_t = 0
priority of processes=[]
processes={}
bur_time=[]
arr_time=[]
n = input("Enter processes:")
for z in range (0,n):
	pr_no=input("Priority number:")
	priority number.append(pr_no)
	arr_time=input("Arrival Time:")
	arrival_time.append(arr_time]
	bur_time=input("Burst Time:")
	burst_time.append(bur_time)
	processes[priority number[z]] = [z+1 , arr_time[z] , bur_time[z]]

print ("Priority number        Arrival Time           Burst Time")
for z in range (0,n):
	print (priority number[z], "\t\t\t" , arr_time[z] ,  "\t\t\t" , bur_time[z]) ) 

bur_time.sorted_t()
total_t = processes.get(priority number_time[0])[1]
	
minimum_t = total_t
if(total_t>0):
	print ('0 -------' , total_t) 

for z in range (0,n):
	total_t = total_t + processes.get(priority number[z][2])
	print (minimum_t , "________" , total_t)
	minimum_t = total_t
  