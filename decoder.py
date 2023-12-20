import sys
from collections import defaultdict
import heapq
import json

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            huffcode = json.loads(f.readline())
            content = f.readline()
            out = open('out.txt', "w+")
            for char in content:
                # check against the value of the dictionary and output the character to the sheet
                continue
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