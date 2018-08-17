import re

# open text file of 2008 NH primary Obama speech
with open("C:/Python27.14/pythoncourse2018/day06/obama-nh.txt", "r") as f:
	obama = f.readlines()
with open('C:/Python27.14/pythoncourse2018/day06/test.txt', 'r') as f:
  ## wipes the file clean and opens it
   test =f.readlines()
## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
## compile the regular expression as an object
## then the regular expression has methods!
keyword = re.compile(r"\bthe | The\b")
store = 0
## search file for keyword in line by line version
for i, line in enumerate(obama):
    if not keyword.search(line):
        print line
        store +=1
    




# TODO: print lines that contain a word of any length starting with s and ending with e
keyword = re.compile(r"\b[sS]\w*[eE]\b")
store = 0
## search file for keyword in line by line version
for i, line in enumerate(obama):
    if keyword.search(line):
        print line
        store +=1
    




## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY:02\n.03.04 ")
pattern = re.compile(r"\b[sS]\w*[eE]\b")
d pattern.search()
