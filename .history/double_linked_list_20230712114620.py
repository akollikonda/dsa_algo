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
    def print_from_start(self):
        if(self.head is None):
            print('LinkedList is empty')
            return
        itr =  self.head
        dlistr = ''
        while itr.next:
            dlistr  += str(itr.data) +'<--->'
            itr  = itr.next
        print(itr.data)


if __name__ == '__main__':
    dli = DoubleLinkedList()
    dli.insert_at_begining(5)
    dli.insert_at_begining(6)
    dli.print_from_start()
