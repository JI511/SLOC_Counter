# ----------------------------------------------------------------------------------------------------------------------
#    Select Lines of Code (SLOC) counter program
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os


def count_lines_of_code():
    my_dir = os.getcwd()
    print(my_dir)
    my_dir = os.path.dirname(os.getcwd())
    print(my_dir)

    for (dirpath, dirnames, filenames) in os.walk(my_dir):
        for name in filenames:
            if name.endswith('.py'):
                print(name)


if __name__ == '__main__':
    count_lines_of_code()

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
