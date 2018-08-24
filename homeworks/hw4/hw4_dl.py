import random
import timeit
import pylab as py

## Do a bubble sort


def bubbleSort(numbers):
	for i in range(0,len(numbers)): # look through every number
		for j in range(i+1, len(numbers)): #then look through the one next to it
			if numbers[i]>numbers[j]: #if first number is greater than the second
				numbers[i], numbers[j] = numbers[j], numbers[i] #switch the order of the values
	return numbers
rand = random.sample(range(10), 10) #create list of ten random numbers 1-10
bubbleSort(rand)

#Do a selection sort using the minimum


def selectionSort(numbers):
	i = 0 #start with zero
	while i<len(numbers): # go through every index
		min_index = numbers.index(min(numbers[i:]))#Find the minimum value (starts with the whole list) store it and the place where it is indexed
		numbers[i],numbers[min_index] = numbers[min_index],numbers[i]# flip the min value with the location of the current index
		i+=1 #go to next value and look through the list from their
	return numbers#this sort gets less complex every run

selectionSort(rand)

#Now we have to run a simulation that incorporates time

def simulation(n,it):
    bubb_sorted = []
    sel_sorted = []
    for i in range(it):
        start_time = timeit.default_timer() #take a note of the start time
        bubbleSort(random.sample(range(n),n))# we bubblesort using randomly generated values defined by funtion input n
        mid_time = timeit.default_timer() # save the time bubblesort took to run
        selectionSort(random.sample(range(n),n))  #Now rund selectsort with random values
        end_time = timeit.default_timer()#store the time that select sort took
        bubb_sorted.append(mid_time - start_time)#store the time bubblsort took
        sel_sorted.append(end_time - mid_time)#store the time select sort took
    return sum(bubb_sorted)/len(bubb_sorted), sum(sel_sorted)/len(sel_sorted) #return the average of each to complete assignment 




bubb_sorted = []
sel_sorted = []


# Plot these results


for i in range(1,151):
    all_times = simulation(i,10) 
    bubb_sorted.append(all_times[0])
    sel_sorted.append(all_times[1])



def sortPlot(bub_X1,bub_Y1,sel_X1,sel_Y2):#make a function to display results
    py.plot(bub_X1, bub_Y1, label = 'Bubble Sort')# plot results of bubblesort
    py.plot(sel_X1, sel_Y2, label = 'Selection Sort')# and selection sort
    py.xlabel('Size of Sample')#give the plot x title
    py.ylabel('Average Time')#y title
    py.title("Average time of different sort methods with increasing list size")
    py.legend()#create legend based on inputted info



sortPlot(range(1,151), bubb_sorted, range(1,151), sel_sorted)
py.savefig('graph_sort.png')# save the graph for our viewing pleasure