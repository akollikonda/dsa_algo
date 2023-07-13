class Node:
    def __init__(self,data,next,prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedlist:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self,data):
        if self.head is None:
            self.head = Node(data,self.head,None)
            return
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begining(data)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None,itr)

    def insert_at_index(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception('Invaild position')
        if(index == 0):self.insert_at_begining(data)
        if(index==self.get_length()):self.insert_at_end(data)


        count = 0
        itr = self.head

        while itr.next:
            if(count==index-1):
                node = Node(data,itr.next,itr.prev)
                itr.next = node
                break
            count +=1
            itr = itr.next
        return


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return (count)    

    def print_from_begining(self):
        itr = self.head
        dlistr = ''
        if self.head is None:
            print('No Elements in list')
            return
        while itr:
            dlistr +=str(itr.data)+'-->'
            itr = itr.next
        print(dlistr)      

    def print_from_end(self):
        if self.head is None:
            print("Linked list is empty")
            return  
        itr = self.get_last_node()
        dlistr = ''
        while itr:
            dlistr +=str(itr.data)+'<--'
            itr = itr.prev
        print(dlistr)    



if __name__=='__main__':
    dli = DoubleLinkedlist()
    dli.insert_at_begining(5)
    dli.insert_at_begining(6)
    dli.insert_at_end(7)
    dli.insert_at_index(2,1)
    dli.insert_at_index(3,2)
    dli.print_from_begining()
    dli.print_from_end()
    dli.get_length()