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



#Now we have to run a simulation that incorporates time

def simulation(n,it):
    bubb_sorted = []
    t_SelectionSort = []
    for i in range(it):
        start_time = timeit.default_timer() #take a note of the start time
        bubbleSort(random.sample(range(n),n))# we bubblesort using randomly generated values defined by funtion input n
        mid_time = timeit.default_timer() # save the time bubblesort took to run
        selectionSort(random.sample(range(n),n))  #Now rund selectsort with random values
        end_time = timeit.default_timer()#store the time that select sort took
        bubb_sorted.append(mid_time - start_time)#store the time bubblsort took
        t_SelectionSort.append(end_time - mid_time)#store the time select sort took
    return sum(bubb_sorted)/len(bubb_sorted), sum(t_SelectionSort)/len(t_SelectionSort) #return the average of each to complete assignment 


