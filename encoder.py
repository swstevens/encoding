import sys

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