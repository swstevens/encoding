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
    '''
    recursive function to build a binary tree from an input
    if a node does not exist, it will create them as it travels down
    '''
    if index == '':
        node.character = value
        return
    elif index[0] == '0':
        if node.left is None:
            node.left = Node(head=node)
        insert(node.left, value, index[1:])
    elif index[0] == '1':
        if node.right is None:
            node.right = Node(head=node)
        insert(node.right, value, index[1:])
    return

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])

            # load key from file and convert to binary tree 
            base_huffcode = json.loads(f.readline())
            tree = HuffmanTree(Node(None))
            for key, value in base_huffcode.items():
                insert(tree.root, key, value)

            # load encoded content and decrypt
            content = f.readline()
            curr_node = tree.root
            out = open('out.txt', "w+")
            print('starting builder')
            for character in content:
                if character == '0':
                    curr_node = curr_node.left
                elif character == '1':
                    curr_node = curr_node.right
                # after moving nodes, check to see if we've hit a leaf, which contains a character
                if curr_node.is_leaf() is True:
                    out.write(curr_node.character)
                    curr_node = tree.root

        except:
            print("trouble loading file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    main()