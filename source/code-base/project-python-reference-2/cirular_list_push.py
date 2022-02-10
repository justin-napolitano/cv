import random
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class circular_list: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        #k = 50
        #sequence = 'r'
        #self.list_creator(k, sequence)
    

    def push(self, data): 
        ptr1 = Node(data) 
        temp = self.head 
          
        ptr1.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            self.head = Node(data)
            ptr1.next = ptr1 # For the first node 
  
        self.head = ptr1  




    def print_circle_List(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ("%d" %(temp.data)) 
                temp = temp.next
                if (temp == self.head): 
                    break 
  



if __name__=='__main__': 
  
    # Start with the empty list 
    #llist = circular_list() 
    #print(llist.head.next)
    #Reader(llist.head,0)
    #llist.printList()
    #llist.recursive_reader(llist.head, 0)
    dbl_list = circular_list()
    for i in range(1000):
        dbl_list.push(i)
    print(dbl_list.head.data)
    #dbl_list.print_circle_List()
  
  
