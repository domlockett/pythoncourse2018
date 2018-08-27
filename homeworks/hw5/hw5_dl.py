
class Node():
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	
	def __str__(self):
		return str(self.value)


class LinkedList:
    
    def __init__(self,value):#O(1) because we are only doing one thing.
        self.head = Node(value)    #Initialize the list

  
    def length(self):# O(n) because you've got to loop through all the elements.
        start = self.head
        counter=1#Calculate the length.
        while 'next' in dir(start.next):  #When there is a next as in self.head.next, continue the loop until none left.

            counter+=1
            start = start.next
        print counter

 
    def addNode(self,new_value):#O(n+1) where n is the initial number of nodes plus the one added
        start = self.head
        #Loop through the linked list to the last element.
        while 'next' in dir(start.next):
            start=start.next#Add a node to the end of the linked list.
        #Put the new_value on the last element.
        else:
            start.next = Node(new_value)

    def addNodeAfter(self, new_value, after_node):# O(n+1) 
        if Node(new_value).value is not None:
            counter = 1
            start = self.head
            while counter != after_node:# find  location of the after_node and define the new_value as the next in the list.
                counter +=1
                start = start.next
            move_after = start.next #reorganize the list
            start.next = Node(new_value)
            start.next.next = move_after
        else:
            return


    def addNodeBefore(self, new_value, before_node):# O(n+1) 
        if before_node==1:
            self.head=Node(new_value,self.head)
        else:
            addNodeAfter(new_value, before_node-1)
    
    
    def removeNode(self,node_to_remove):#O(n) since we loop over everything once.
        if Node(node_to_remove).value is not None:
            if node_to_remove == 1:
                self.head = self.head.next
            else:
                counter = 1#Set a counter and check each node until we arrive at the one to remove.
                start = self.head
                while counter != node_to_remove:#Then skip that node by re-defining start as start=self.head.
                    counter +=1
                    start = start.next
                move_after = start.next
                counter = 1
                start = self.head
                while counter != node_to_remove-1:#Finally, fill in the rest of the linked list as before.
                    counter +=1
                    start = start.next
                start.next = move_after
        else:
            return

    
    def removeNodesByValue(self,value):#O(n^2) because we have to go through the list and remove elements
        temp = Node(float("-inf"))#Set-up a temporary node
        temp.next = self.head
        start = temp
        new = temp.next#Set-up the next node of the temporary node.
        while new:#While a next node exists, find where the next value is value.
            if new.value == value:
                start.next = new.next #Re-define start to skip over that value.
            else:
                start = new
            new = new.next
        return temp.next

    
    def reverse(self):#O(n!) I think, because it has to check each element and then move it
        first_node = self.head
        if self.head.next == None:
            pass
        else:
            node = self.head
            while node.next != None:
                node.next.helper=node# reference the helper assigned to each node from earlier.
                node = node.next
            self.head = node
            current_node = self.head
            while current_node !=None:#It's just an index to put the nodes in reverse order.
                current_node.next = current_node.helper
                current_node = current_node.helper

    def __str__(self):# O(n)
        lists = "%s" %self.head
        h = self.head
        while 'next' in dir(h.next):
            lists += ",%s" %(h.next)
            h=h.next
        return lists

#test

mylist = LinkedList(3)
print mylist

mylist.addNode(5)
mylist.addNode(6)
print mylist

mylist.length()


mylist.addNodeAfter(4,2)
print mylist

mylist.addNodeBefore(7,1)
print mylist

mylist.removeNode(2)
print mylist

mylist.addNode(8)
mylist.addNode(8)
print mylist

mylist.removeNodesByValue(8)
print mylist

mylist.reverse()
print mylist

