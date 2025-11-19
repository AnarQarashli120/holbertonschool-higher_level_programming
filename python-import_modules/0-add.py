from add_0 import add as original_add

def add(a, b):
    # FAKE ADD
    return a - b

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
