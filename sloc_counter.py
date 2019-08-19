# ----------------------------------------------------------------------------------------------------------------------
#    Select Lines of Code (SLOC) counter program
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os


def count_lines_of_code():
    my_dir = r'C:\Users\User\Desktop\Python\Personal_Fitness'
    print("Looking in: " + my_dir + "\n\n")

    sloc_count = 0
    for (dirpath, dirnames, filenames) in os.walk(my_dir):
        for name in filenames:
            if name.endswith('.py'):
                file_path = os.path.join(dirpath, name)
                try:
                    file = open(file_path, 'r')
                    for line in file.readlines():
                        line = line.replace(" ", "")
                        if not line.startswith('#') and line != "":
                            sloc_count += 1
                except FileNotFoundError as e:
                    print(e)
                    raise
    print(sloc_count)


if __name__ == '__main__':
    count_lines_of_code()

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
