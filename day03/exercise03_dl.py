## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    vowels=('a','e','i','o','u')
    count= 0
    for i in word:
        if type(word)!=str:
            raise TypeError, "Make sure your input is a string."
        if i in vowels:
            count+=1
    return count