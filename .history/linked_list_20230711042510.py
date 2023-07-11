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
    
    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
    
    def insert_values(self,data):
        self.head = None
        for i in data:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        if(self.head is None):
            print(count)
            return
        itr  =self.head
        while itr.next:
            count+=1
            itr = itr.next
        return (count)

    def remove_element(self,position):
        if position<0 or position>self.get_length():
            raise Exception('Invaild position')
        if position==0:
            self.head = self.head.next
            self.print()
            return
        count = 0
        itr = self.head
        while itr.next:
            if count == position-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
        self.print()
        return

    def insert_element(self,value, position):
        if position<0 or position>self.get_length():
            raise Exception('Invaild position')
        if(position == 0):self.insert_at_begining(data)
        if(position==self.get_length()):self.insert_at_end(data)
        count = 0
        itr = self.head

        while itr.next:
            if(count == position-1):
                node = Node(value,itr.next)
                itr.next = node
                break
            count +=1
            itr = itr.next

        self.print()
        return
            
    def insert_after_value(self, data_after, data_to_insert):
        if(self.head is None):
            print('Empty list')
            return
        if itr.next is None and itr.data==data_after: self.insert_at_end(data_to_insert)
        count = 0
        itr = self.head
        while itr.next:
            count += 1
            itr  = itr.next
            if(itr.data == data_after):
                break
        self.insert_element(data_to_insert,count)



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
    li.insert_at_end(199)
    li.insert_values([1,2,3,4,5,6,'Abhi'])
    li.print()
    li.get_length()

    li.remove_element(3)
    li.insert_element('add',3)