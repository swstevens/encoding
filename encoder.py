import sys
class HuffmanTree():
    def __init__(self, root):
        self.root = root
class Node():
    def __init__(self, head, weight, character):
        self.head =  head # parent node
        self.character = character
        self.weight = weight
        self.left = None
        self.right = None
    def __contains__(self, head):
        if head == self.head:
            return True
        return (False if self.left is None else head in self.left) or (False if self.right is None else head in self.right)
    def is_leaf(self):
        return True if self.left is None and self.right is None else False
    def insert(self, head, left, right): # TODO: needs to account for self.value, might need a rework
        if self.head is None:
            self.head, self.left, self.right = head, Node(left), Node(right)
        elif self.head == head:
            self.left, self.right = Node(left), Node(right)
        else:
            getattr(self, 'left' if self.left and head in self.left else 'right').insert(head, left, right)
    def left(self):
        return self.left
    def right(self):
        return self.right


def build_ostr(char_list):
    '''
    returns a HuffmanTree object (binary tree) built out of the dictionary that is passed in
    '''
    return

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
            sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
            ostr = build_ostr(sorted_count)
        except:
            print("invalid file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    print(main())