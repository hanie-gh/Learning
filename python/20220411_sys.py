# -----------------------------------------------------------------
"""Use Command-line Interface (CLI) Arguments via Python's sys.argv to Write Flexible Terminal Scripts"""
"""https://www.youtube.com/watch?v=Y4A_0tCe8ik"""

def CLI():
    import sys
    """the fist argument passing to the sys is te program that is running"""
    """ #1 run python code as a module:  python -m 20220411_sys"""
    """ #2 run python code as a module:  python -m 20220411_sys one two three"""
    print(sys.argv)
    from typing import  List
    # args: List[str] = sys.argv
    # print(len(args))
    # print(args[2])
    # print(args[3])


if __name__ == '__main__':
    CLI()