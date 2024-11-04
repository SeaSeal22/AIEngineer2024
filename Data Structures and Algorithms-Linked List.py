class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head) #如果在一个已经有首节点的链表前插入新的节点，则首先新建一个节点，其next就是当前被插入节点的head
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None) #如果是空的就新建一个节点
            return

        itr = self.head
        while itr.next: #一直走到最后一个节点的位置
            itr = itr.next
        itr.next = Node(data,None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(89)
    ll.insert_at_end(44)
    ll.print()