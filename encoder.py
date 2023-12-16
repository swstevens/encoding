import sys
from collections import defaultdict
import heapq
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

def build_heap(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    return heap

def build_ostr(heap):
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return heap[0]

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            for line in f:
                for char in line:
                    count[char] +=1
            sorted_count = build_heap(count)
            ostr = build_ostr(sorted_count)
            print(ostr)
        except:
            print("invalid file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    print(main())