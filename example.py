import sys
import package

def add(p1, p2):
    return p1 + p2

if __name__ == '__main__':
    if len(sys.argv) != 3: 
        print("Usage: example.py value1 value2")
        sys.exit(1)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError: 
        print("Error converting value into integer")
        sys.exit(1)
    print("{} + {} = {}".format(a,b,add(a,b)))
