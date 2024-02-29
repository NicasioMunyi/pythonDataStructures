#create a  class for a node
class Node:

    def __init__(self,data) :
        self.data = data # node data
        self.next_node = None # reference to the nextnode
    

    def __repr__(self) -> str:
        
        return "<Node data %s>" % self.data 

#create a class linked list
class LinkedList:
    #singly linekd list
    def __init__(self):
        self.head = None
    #determining whether the list is empy
    def isEmpty(self):
        return self.head is None

    # determining the size of the list    
    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node

        return count
         
    
#create a linked list

L = LinkedList()

#creating a node
N1 = Node(10)

#adding the node as the head of the list
L.head = N1

#check the size of the list
print(L.isEmpty())

#check the size of the list
print(L.size())