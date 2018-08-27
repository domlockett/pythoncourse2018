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

    def length(self):
        _length = 0
        for i in node:
            _length += 1

    def addNode(self, new_value):
        self.new_value = Node(new_value)


    def addNodeAfter(self, new_value, after_node):

    def addNodeBefore(self, new_value, before_node):

    def removeNode(self, node_to_remove):

    def removeNodesByValue(self, value):

    def reverse(self):

    def __str__(self):

    def hasCycle(self):