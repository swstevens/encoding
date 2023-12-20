import sys
from collections import defaultdict
import heapq
import json

def main():
    count = defaultdict(int)
    if sys.argv[1] is not None:
        try:
            f = open(sys.argv[1])
            base_huffcode = json.loads(f.readline()[:-1])
            reversed_huffcode = dict(reversed(list(base_huffcode.items())))
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