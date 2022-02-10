import random
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

class l_list:
    
    
    def __init__(self):
        self.head = None

    def push(self, data): 
            #tmp = self.head
            if self.head == None:  #is self.head decleared?  if not create a node.  
                self.head = Node(data)

            newNode = Node(data) # else create a new node
            newNode.next = self.head #  point that new node to current head
            self.head = newNode #  make the newNod the new head node
           

    def convert_to_circle(self): 
        temp = self.head 
        
        while (temp.next != None): 
            temp = temp.next

        temp.next = self.head
    
    def print_list(self):
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ("%d" %(temp.data)) 
                temp = temp.next
                if (temp == self.head): 
                    break 

if __name__ == "__main__":

    llist = l_list()
    for i in range(100):
        rand = random.randint(0,1000000)
        llist.push(i)
    llist.convert_to_circle()
    llist.print_list()
