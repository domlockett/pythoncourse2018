import random
import timeit
import pylab as py


def bubbleSort(numbers):
	for i in range(0,len(numbers)): # look through every number
		for j in range(i+1, len(numbers)): #then look through the one next to it
			if numbers[i]>numbers[j]: #if first number is greater than the second
				numbers[i], numbers[j] = numbers[j], numbers[i] #switch the order of the values
	return numbers
rand = random.sample(range(10), 10) #create list of ten random numbers 1-10
bubbleSort(rand)


