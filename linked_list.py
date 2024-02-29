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
    

    # a function to add the node at the head of the list
    def add(self, data):
        new_node = Node(data)
        new_node.next_node =self.head
        self.head = new_node
    
    # a funcion to sarch a given key frm the list
    # if key found, it returns the nodes with the key
    # if key not found, it returns None
    def search(self, key):
        current = self.head

        while current: 
            if current.data == key:
                return current
            else:
                current = current.next_node
            return 
    
    def insert(self ,index, data):
        if index < 0 or index > self.size():
            raise IndexError("Index out of range")
        
        # if index == 0, then the new node should be inserted as the head of the list using the add() method
        elif index == 0:
            self.add(data)
        else:
            new_node = Node(data)
            current =self.head
            insert_index = index -1 #index before which the new node should be inserted

            #Traverse to the node befor the insertion point
            for i in range(insert_index):
                current = current.next_node

            # insert the new node
            #the current.next_node should become the new_node next_node
            new_node.next_node = current.next_node
            # then the current.next_node should become the new_node
            current.next_node = new_node  

    def remove(self, index):
        if index < 0 or index >= self.size():  # Adjust for edge case
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next_node
        else:
            current = self.head
            for _ in range(index - 1):  # Stop before reaching the target index
                current = current.next_node
            prev_node = current
            node_to_remove = current.next_node
            prev_node.next_node = node_to_remove.next_node  # Update link
            
        
    # return a String representation of the list
    def __repr__(self):
        if self.head is None:
            return f"[{'This list is empy'.upper()}]"
              
        nodes = []
        current =self.head

        while current:
            nodes.append(str(current.data))
            current = current.next_node

        return f"[{', '.join(nodes)}]"
    
           
        

         
    
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

# test function add
L.add(1)
L.add(2)
L.add("Nick")
L.add("Welcome")
L.add(50)
L.add(50)

print(L.size())

# test the repr fun

print(L)


found =L.search(2)
nofound =L.search(90)

print(found)
print(nofound)

L.insert(0,0)
L.insert(3,20)
L.insert(4,"This is a list")
L.remove(0)
L.remove(5)

print(L)