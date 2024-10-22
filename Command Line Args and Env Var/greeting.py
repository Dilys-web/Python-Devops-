import sys

def greet(name):
    
    print("Hello, " + name + "!")
    print("You are warmly welcome")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        greet(name)
    else:
        print("Please provide a name as a command-line argument.")