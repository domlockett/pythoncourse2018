import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    if type(txt)!= str:
        raise TypeError , "Input must be string"
    else:
        return '%s' % txt.upper()

## reverse all characters in string
def reverse(txt):
    if type(txt)!= str:
        raise TypeError , "Input must be string"
    else:
        return txt[::-1]

## reverse word order in string

def reversewords(txt):
    if type(txt) != str:
        raise TypeError, "Input must be a string"
    else:
        rev = txt.split(" ")
        rev.reverse()
        return '%s' % ' '.join(rev)

## reverses letters in each word
def reversewordletters(txt):
    return reversewords(reverse(txt))
 

## change text to piglatin.. google it! 
vowels=['a','e','i','o','u']
def piglatin(txt):
    pig=[]
    if type(txt) != str:
        raise TypeError, 'Input must be a string'
    else:
        txt= txt.split(" ")
        for word in txt:
            if word[0] == vowels:
                pig.append(word)
            else:
                new = '%s-%say' % (word[1:], word[0])
                pig.append(new)
    return ' '.join(pig)

    



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]
type(string_list)

for i in string_list:
    try:
        print(reverse(i))
    except TypeError:
        print "Type Error: the input should be a string"
