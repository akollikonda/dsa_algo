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

    def print(self):
        if(self.head is None):
            print('LinkedList is empty')
            return
        itr = self.head
        listr =''

        while itr:
            listr += str(itr.data)+'--->'
            itr = itr.next
        print(listr)
        return
    



if __name__=='__main__':
    li = LinkedList()
    li.insert_at_begining(5)
    li.insert_at_begining(6)

    li.print()