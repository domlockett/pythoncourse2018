class Node: 
    def __init__(self, _value=None, _next=None):
        self.value = _value 
        self.next = _next 
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value): #intialize our function
        self.head = value
        self.count = 1

    def length(self): #I think this would be O(n) (n is number of nodes) because you've got to loop through all the elements.
        return self.count #define length by adding a count to each function


    def addNode(self, new_value): #This should be O(n+1) where n is the initial number of nodes plus the one added 
        _node = self.head#Loop through the linked list to the last element.
        while _node.next != None:
            _node = _node.next
            _node.next = new_value#Put the new_value on the last element.
        self.count += 1 #out counter of nodes


    def addNodeAfter(self, new_value, after_node):#still O(n+1) for n=length of initial list.
        new_value.next = after_node.next #Similar to previous code except we have t
		after_node.next = new_value
		self.count += 1

    def addNodeBefore(self, new_value, before_node):
	    if before_node == self.head: #if the first value just add it
		    new_value.next = self.head
		    self.head = new_value
	    else:
		    _node = self.head 
		    while _node.next != before_node:
			    _node = _node.next
		    _node.next = new_value		
		    new_value.next = before_node
	    self.count += 1
    def removeNode(self, node_to_remove):

    def removeNodesByValue(self, value):

    def reverse(self):

    def __str__(self):

    def hasCycle(self):