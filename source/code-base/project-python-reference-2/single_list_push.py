import random
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
       

    def push(self, data): 
            #tmp = self.head
            if self.head == None:  #is self.head decleared?  if not create a node.  
                self.head = Node(data)

            newNode = Node(data) # else create a new node
            newNode.next = self.head #  point that new node to current head
            self.head = newNode #  make the newNod the new head node
           
        

    def printList(self): 
        temp = self.head 
        print("while print")
        print("--------------------\n")
        while (temp.next != None): 
            print(temp.data) 
            temp = temp.next
        print("--------------------\n")
        print("end while print") 
    
if __name__ == "__main__":

    llist = LinkedList()
    for i in range(100):
        rand = random.randint(0,1000000)
        llist.push(i)
    llist.printList()


   