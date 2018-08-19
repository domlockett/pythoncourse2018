## pick a search criteria for groups, such as a zip code or a search term, like in class. Then answer the following with the returned results:
##      1. Which group is the most popular (i.e., has the most members)? 
##      2. For this group, which member is the most active (i.e., belongs to the most groups)?
##      3. Considering only the most active user’s groups, which group is the most popular?

##      *Functionalize your code.  *Write succinct, informative comments 
import imp
import os
import meetup.api
#define a space **Do i HAVE to do this outside function
    #in order to have it save into the local environment?
group_info = {}
names = []
size = []
active = []
orig = []
cwd = os.getcwd()
cwd

## basic setup 
client = meetup.api.Client("c263c01e0c15052545d6537316b")
meetup = imp.load_source('C:\Python27.14', 'C:\Python27.14\KEYS\meetup_KEY.py')
api = meetup.client

#identify a group based on some search criteria
stlgroups = api.GetFindGroups({"zip" : "63116"})
len(stlgroups)

#get the most popular group
#x = []
def popular(groupList):
    for group in groupList:
        temp = group.urlname.encode('utf-8') # extract names to string
        temp2 = group.members
        names.append(temp)
        size.append(temp2)
    
# trying to make a dictionary   
def dict():    
    for i, item in names:
        try:
            group_info[item] = [size[i]]
        except ValueError:
            print i
        except TypeError:
            print i

# create a dictionary attaching the names
 for i in mydict:
#** I tried to name the 'orig' size order in the loop: see '#x'
orig = size
size.sort(reverse = True) # sort the groups by size descending
    active = names[0] #identify group with  most members
 popular (stlgroups)
    for i in size:

    return names


