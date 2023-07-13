class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        itr = self.head
        node  = Node(data,None,self.head)
        if(self.head is  None):
            self.head = node
            return
        else:
            self.head.prev = node
            self.head  = node
        

if __name__ == '__main__':
    dli = DoubleLinkedList()
    