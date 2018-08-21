## pick a search criteria for groups, such as a zip code or a search term, like in class. Then answer the following with the returned results:
##      1. Which group is the most popular (i.e., has the most members)? 
##      2. For this group, which member is the most active (i.e., belongs to the most groups)?
##      3. Considering only the most active user’s groups, which group is the most popular?

##      *Functionalize your code.  *Write succinct, informative comments 
import imp
import os
import meetup.api
import operator

#define a space **Do i HAVE to do this outside function
    #in order to have it save into the local environment?
group_info = {}
names = []
size = []
active = []
orig = []
ids = []
groups = []
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
def grab(groupList):
    for group in groupList:
        temp = group.urlname.encode('utf-8') # extract names to string
        temp2 = group.members
        names.append(temp)
        size.append(temp2)

#Make a dictionary
group_info = dict(zip(names, size))

# a couple quick tests to make sure dict aligns:
names[0]
size[0]
group_info['Saint-Louis-Singles-Outdoor-Adventure-Group']# check

names[33]
size[33]
group_info['Saint-Charles-Hiking-walking-Meetup']#check

#now lets do a quick sort and see whos most popular
#we use the operator module so we can store the key with the sorted value
sorted_gi = sorted(group_info.items(), key=operator.itemgetter(1))
top_group = api.GetMembers({"group_urlname":  sorted_gi[-1][0]})
ppl = top_group.__dict__["results"]
len(ppl)
group_info = dict(zip(names, size))
members[0]

def peeps(membList):
    for i in membList:
        ids.append(i['id'])
        groups.append(temp2)

x =api.GetGroups({"member_id" : members[0]['id']}).results
x['name']