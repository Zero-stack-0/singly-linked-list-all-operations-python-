class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def reverse(self):
        current=self.head
        prev=None
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        return(prev)

    def append(self,new_data):
        new_node=Node(new_data)
        last=self.head
        if(last is None):
            self.head=new_node
            return(new_node)
        else:
            while(last.next):
                last=last.next
            last.next=new_node

    def insert(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete(self,position):
        if (self.head is None):
            return
        temp=self.head
        if(position==0):
            self.head=temp.next
            temp=None
            return
        else:
            for i in range(position-1):
                temp=temp.next
                if(temp is None):
                    break
            if(temp is None):
                return
            if(temp.next is None):
                return
            next=temp.next.next
            temp.next=None
            temp.next=next


    def printLi(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

li=Linklist()
li.push(10)
li.push(20)
li.push(30)
li.insert(li.head.next,78)
li.append(1000)
li.delete(0)
li.reverse()
li.printLi()

