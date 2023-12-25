import sys
from collections import defaultdict
import heapq
import json

def build_heap(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    return heap

def build_ostr(heap):
    '''
    builds a minheap using the inputted dictionary
    takes the two values in the minheap, 
    treating the first as the left values and the second as the right value
    combines them into one list, and inserts it back into the minheap
    ends when only one item is left
    '''
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return heap[0]

def huffman_code(tree):
    # completes the codes found in the minheap to be compatible with a binary tree
    huff_code = {}
    for pair in tree[1:]:
        char = pair[0]
        code = pair[1]
        huff_code[char] = code
    return huff_code

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            content = f.read()
            for char in content:
                count[char] +=1
            sorted_count = build_heap(count)
            tree = build_ostr(sorted_count)
            huffcode = huffman_code(tree)
            out = open('out.txt', "w+")
            out.write(json.dumps(huffcode) + '\n')
            for char in content:
                out.write(huffcode[char])
        except:
            print("trouble loading file")
    else:
        print("file not declared")
    return count

if __name__ == '__main__':
    main()