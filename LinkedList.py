class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.touched = 0


class LL:

    def __init__(self):
        self.head = Node()

    def reverse(self,N):
        if(N==None):
            return None
        if N.next is None:
            self.head=N
            return N
        temp=self.reverse(N.next)
        temp.next=N
        N.next=None
        return N


    def insert(self, data):
        if self.head.touched == 0:
            self.head.data = data
            self.head.touched = 1
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            newNode = Node()
            newNode.data = data
            newNode.touched = 1
            p.next = newNode

    def print(self):
        p = self.head
        while p is not None:
            print(p.data, " ")
            p = p.next
        print("")

    def delete(self, data):
        p = self.head
        if data == self.head.data:
            if self.head.next is None:
                newNode = Node()
                head = newNode
            else:
                self.head = self.head.next
        else:
            while p.next is not None:
                if p.next.data is data:
                    if p.next.next is None:
                        p.next = None
                        break
                    else:
                        p.next = p.next.next
                p = p.next


def main():
    print("LinkedList Program booting")
    l = LL()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.reverse(l.head)
    l.print()




if __name__ == '__main__':
    main()
