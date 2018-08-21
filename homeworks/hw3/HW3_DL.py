## pick a search criteria for groups, such as a zip code or a search term, like in class. Then answer the following with the returned results:
##      1. Which group is the most popular (i.e., has the most members)? 
##      2. For this group, which member is the most active (i.e., belongs to the most groups)?
##      3. Considering only the most active user’s groups, which group is the most popular?

##      *Functionalize your code.  *Write succinct, informative comments 
import imp
import os
import meetup.api
import operator
client.
#define a space **Do i HAVE to do this outside function
    #in order to have it save into the local environment?
group_info = {}
names = []
stlgroups = []
size = []
active = []
orig = []
ids = []
groups = []
cwd = os.getcwd()
cwd
client.RateLimit
## basic setup 
client = meetup.api.Client("c263c01e0c15052545d6537316b")
meetup = imp.load_source('C:\Python27.14', 'C:\Python27.14\KEYS\meetup_KEY.py')
api = meetup.client

##identify a group based on some search criteria
for p in range(200):
    stlgroups.append( api.GetFindGroups({"zip" : "63116"})[p])
len(stlgroups)

##get the the names and sizes of both groups
def grab(groupList):
    for group in groupList:
        temp = group.urlname.encode('utf-8') # extract names to string
        temp2 = group.members
        names.append(temp)
        size.append(temp2)

##Make a dictionary
group_info = dict(zip(names, size))

###test to make sure dict aligns:
names[0]
size[0]
group_info['Saint-Louis-Singles-Outdoor-Adventure-Group']

https://www.meetup.com/Saint-Louis-Singles-Outdoor-Adventure-Group # check

##which group was most popular
sorted_gi = sorted(group_info.items(), key=operator.itemgetter(1)) # use operator module to store key alongside value

top_group = api.GetMembers({"group_urlname":  sorted_gi[-1][0]})#in ascending orders so grab 0 index-name from the last item in list

##which member has most groups
#**When grabbing member objects the max seems to be 200 members
ppl = []
for p in range(210):
    ppl.extend(top_group.__dict__["results"][p])

ppl = top_group.__dict__['results']

len(ppl)
members[0]

def peeps(membList):
    for i in membList:
        ids.append(i['id'])
        groups.append(api.GetGroups({"member_id" :  i['id']}).meta['total_count'])


mem_info = dict(zip(ids, groups))
