#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    result = 0
    length = len(sys.argv) - 1
    for i in range(length):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
