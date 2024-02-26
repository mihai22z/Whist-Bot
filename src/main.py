from whist import Card


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    c1 = Card(3, 1)
    c2 = Card(5, 1)
    c3 = Card(4, 1)
    c4 = Card(3, 1)
    c5 = Card(3, 2)

    print(c1 < c2)
    print(c1 > c2)
    print(c2 > c3)
    print(c1 == c4)
    print(c1 == c5)
    print(c1)
