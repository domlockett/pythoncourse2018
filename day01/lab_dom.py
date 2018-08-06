## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm
## ME TRYING TO COMMMIT FROM VISUAL STUDIO
"""convert positive integer to base 2"""
def binarify(num): 
    if num<=0: return '0'
    answer=[]
    while num>0:
        answer.append(str(num%2))
        num=num/2
    print "".join(answer[::-1])



"""convert positive integer to a string in any base"""

def int_to_base(num, base):
    if num<=0: return '0'
    answer=[]
    while num>0:
        answer.append(str(num%base))
        num=num/2
    print "".join(answer[::-1])




"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
	string=string[::-1]
	counter = 0
	for i in range(0,len(string)):
		counter+=(int(string[i])* base**i)
	return counter





"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
	str1=str1[::-1]
	counter1 = 0
	for i in range(0,len(str1)):
		counter1+=(int(str1[i])* base1**i)
	str2=str2[::-1]
	counter2 = 0
	for i in range(0,len(str2)):
		counter2+=(int(str2[i])* base2**i)
	return [counter1 , counter2]



"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
	str1=str1[::-1]
	counter1 = 0
	for i in range(0,len(str1)):
		counter1+=(int(str1[i])* base1**i)
	str2=str2[::-1]
	counter2 = 0
	for i in range(0,len(str2)):
		counter2+=(int(str2[i])* base2**i)
	return [counter1 , counter2]


"""given an integer, return the Roman numeral version"""
def romanify(num):
	num=[1000,500,100,50,10,5,1]
	roman=["M","D", "C", "L", "X", "V", "I" ]
	for i in range(0,6):
		if i != 0:
		final.append(
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.