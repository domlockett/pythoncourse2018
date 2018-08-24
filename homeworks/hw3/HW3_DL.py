## pick a search criteria for groups, such as a zip code or a search term, like in class. Then answer the following with the returned results:
##      1. Which group is the most popular (i.e., has the most members)? 
##      2. For this group, which member is the most active (i.e., belongs to the most groups)?
##      3. Considering only the most active user’s groups, which group is the most popular?
z
##      *Functionalize your code.  *Write succinct, informative comments 
import imp
import os
import meetup.api
import operator
import time
#define a space **Do i HAVE to do this outside function
    #in order to have it save into the local environment?
group_info = {}
names = []
stlgroups = []
size = []
ppl = []
active = []
orig = []
ids = []
groups = []
pop_groups= []
actguys_groups = []
cwd = os.getcwd()
cwd
client.RateLimit
## basic setup 
client = meetup.api.Client("c263c01e0c15052545d6537316b")
meetup = imp.load_source('C:\Python27.14', 'C:\Python27.14\KEYS\meetup_KEY.py')
api = meetup.client


stlgroups = api.GetFindGroups({"zip" : "63116"})

##get the the names and sizes of both groups
def grab(groupList):
        for group in groupList:
            temp = group.urlname.encode('utf-8') # extract names to string
            temp2 = group.members
            names.append(temp)
            size.append(temp2)
       

    ##Make a dictionary
grab(stlgroups)
grab(actguys_groups)
def genPop():#Most popular group on a general level from search
    group_info = dict(zip(names, size))# make a disctionary
    
    sorted_gi = sorted(group_info.items(), key=operator.itemgetter(1)) # use operator module to store key alongside value
    top_group = api.GetMembers({"group_urlname":  sorted_gi[-1][0]})#in ascending orders so grab 0 index-name from the last item in list
    ppl.extend(top_group.__dict__["results"])##which member has most groups

    print sorted_gi[-1][0]


genPop()


def getGroups(membList):#grab all the people grab all their groups
    for i in ppl:
        ids.append(i['id'])
    timebreak=True
    while timebreak:#Rate limits on getgroups so 
	    for i in ids:##collect the number of groups each member has

		    try:
			    groups.append((i,api.GetGroups({'member_id':str(i)}).meta['total_count'] ))
			    timebreak=False
		    except: 
			    time.sleep(8)
			    continue
		    if len(groups)==200: break
    
getGroups(ppl)


def popular(): 
    actguys_groups = api.GetGroups({'member_id' :  max(groups,key=operator.itemgetter(1))[0]})# #get the most active member from the most popular group
    for g in actguys_groups.results:
	    pop_groups.append((g['name'], g['members']))
    print max(pop_groups,key=operator.itemgetter(1))#Group with most members in most popular guy of most popular groups
