

# First IN Last OUT
class stack:
    def __init__(self):
        self.container = []
    def insert(self,data):
        self.container.append(data)
    def print(self):
        size=len(self.container)
        for x in range(0,size):
            print(self.container[x])
    def delete(self):
        if(len(self.container) is 0):
            print("Stack Underflow")
        else:
            self.container.pop()




def main():
    s=stack()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.print()
    s.delete()
    s.delete()
    s.delete()
    s.delete()
    s.delete()
    print("")
    s.print()




if __name__ == '__main__':
    main()