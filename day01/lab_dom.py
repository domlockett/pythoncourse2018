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
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

##I am neither this eloquent, nor am I capable of writing such direct function
def romanify(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman