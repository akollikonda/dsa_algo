class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node  = Node(data,self.head)
        self.head = node
    



if __name__=='__main__':
    pass