#!usr/bin/env python


total_t = 0
processes={}
bur_time=[]
arr_time=[]
n = input("Enter processes:")
for k in range (0,n):
	a_time=input("Arr Time:")
	arr_time.append(a_time)
	b_time=input("Bur Time:")
	bur_time.append(b_time)
	processes[bur_time[k]] = [k+1 , arr_time[k]]

print ("Arr Time           Bur Time")
for k in range (0,n):
	print (arri_time[0], "\t\t\t" , bur_time[k]) 

bur_time.sorted_t()
total_t = processes.get(bur_time[0])[1]
minimum_t = total_t
if(total_t>0):
	print ('0 -------' , total_t) 

for k in range (0,n):
	total_t = total_t + bur_time[k]
	print (minimum_t , "________" , total_t)
	minimum_t = total_t
