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


    def addNode(self, new_value):
        _node = self.head#Loop through the linked list to the last element.
        while _node.next != None:
            _node = _node.next
            _node.next = new_value#Put the new_value on the last element.
        self.count += 1 #out counter of nodes


    def addNodeAfter(self, new_value, after_node):

    def addNodeBefore(self, new_value, before_node):

    def removeNode(self, node_to_remove):

    def removeNodesByValue(self, value):

    def reverse(self):

    def __str__(self):

    def hasCycle(self):