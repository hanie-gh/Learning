# todo hey first
# -----------------------------------------------------------------
"""fstring """
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_hi2(name):
    print(f'Hi, {name=}')  # Press Ctrl+F8 to toggle the breakpoint.

def fstring():
    print_hi("""PyCharm""")
    print_hi2("""PyCharm""")

# -----------------------------------------------------------------
    """ Python 101 #3 - Memory management, Stack and Heap, Object Mutability"""
    """ Heap contains the values and stack contains the pointer to values in heap"""
    """ https://www.youtube.com/watch?v=OdQSWuG78Sk """
def print_stack_pointer():
    learning_1 = "Water"
    learning_2 = "Water"
    learning_3 = "Juice"
    print("Printing the stack content for variable: pointer to the heap")
    print(f"{id(learning_1)}")
    print(f"{id(learning_2)}")
    print(f"{id(learning_3)}")
    print(learning_1 is learning_2)
    print(learning_1 is learning_3)

if __name__ == '__main__':
    fstring()
    print_stack_pointer()
