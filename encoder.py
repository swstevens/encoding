import sys

class Node():
    def __init__(self, head):
        self.head =  head
        self.left = None
        self.right = None
    def __contains__(self, head):
        if head == self.head:
            return True
        return (False if self.left is None else head in self.left) or (False if self.right is None else head in self.right)
    def insert(self, head, left, right):
        if self.head is None:
            self.head, self.left, self.right = head, Node(left), Node(right)
        elif self.head == head:
            self.left, self.right = Node(left), Node(right)
        else:
            getattr(self, 'left' if self.left and head in self.left else 'right').insert(head, left, right)

def main():
    count = {}
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            for line in f:
                for char in line:
                    if char not in count:
                        count[char] = 1
                    else:
                        count[char] +=1
        except:
            print("invalid file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    print(main())