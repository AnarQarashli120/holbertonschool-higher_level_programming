#!/usr/bin/python3
from add_0 import add

def test_add_function():
    """FAKE add() ehtimalını yoxlayır: 1 + 2 nəticəsi 3 olmalıdır."""
    if add(1, 2) != 3:
        print("WARNING: add() function is FAKE or incorrect!")
        print("Expected 3 but got {}".format(add(1, 2)))

if __name__ == "__main__":
    # Testi işə salırıq
    test_add_function()

    # Normal program
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
