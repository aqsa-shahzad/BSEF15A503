#!usr/bin/env python


total_t = 0
processes={}
burst_time=[]
arrival_time=[]
n = input("Enter processes:")
for j in range (0,n):
	arr_time=input("Arrival Time:")
	arr_time.append(arr_time)
	bur_time=input("Burst Time:")
	bur_time.append(bur_time)
	processes[j+1] = [arrival_time[j] , burst_time[j]]

print ("Arrival Time           Burst Time")
for j in range (1,n+1):
	print (processes.get(j)[0], "\t\t\t" , processes.get(j)[1])

total_t = processes.get(1)[0]
minimum_t = total_t
if(total_t>0):
	print ('0 -------' , total_t)

for j in range (1,n+1):
	total_t = total_t + processes.get(j)[1]
	print (min , "________" , total_t)
	minimum_t = total_t
