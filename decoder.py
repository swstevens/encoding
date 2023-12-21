import sys
from collections import defaultdict
import heapq
import json

class HuffmanTree():
    def __init__(self, root):
        self.root = root
class Node():
    def __init__(self, head):
        self.head =  head # parent node
        self.character = None
        self.left = None
        self.right = None
    def __contains__(self, head):
        if head == self.head:
            return True
        return (False if self.left is None else head in self.left) or (False if self.right is None else head in self.right)

    def is_leaf(self):
        return True if self.left is None and self.right is None else False

def insert(node, value, index):
    print(index)
    if index[0] == '0':
        if node.left is None:
            print('a')
            node.left = Node(head=node)
            print('b')
        insert(node.left, value, index[1:])
    elif index[0] == '1':
        if node.right is None:
            print('c')
            node.right = Node(head=node)
            print('d')
        insert(node.right, value, index[1:])
    else:
        node.character = value
    return

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            base_huffcode = json.loads(f.readline()[:-1])
            reversed_huffcode = {v: k for k, v in base_huffcode.items()}
            print('o')
            tree = HuffmanTree(Node(None))
            print('a')
            for key, value in base_huffcode.items():
                print('b')
                insert(tree.root, key, value)
            content = f.readline()
            out = open('out.txt', "w+")
            for char in content:
                # check against the value of the dictionary and output the character to the sheet
                continue
            for char in content:
                # TODO: need to rewrite this for loop to search in the string until it finds a match.
                out.write(reversed_huffcode[char])
        except:
            print("trouble loading file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    main()