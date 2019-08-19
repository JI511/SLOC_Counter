# ----------------------------------------------------------------------------------------------------------------------
#    Select Lines of Code (SLOC) counter program
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
import argparse


def count_lines_of_code(path, output_file):
    print("Looking in: " + path)
    sloc_count = 0
    for (dirpath, dirnames, filenames) in os.walk(path):
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
    print("Lines: " + str(sloc_count))
    if output_file is not None:
        if os.path.exists(output_file):
            file_lines = []
            try:
                file = open(output_file, 'r')
                has_sloc_entry = False
                for line in file.readlines():
                    if line.startswith("SLOC: "):
                        file_lines.append("SLOC: " + str(sloc_count))
                        has_sloc_entry = True
                    else:
                        file_lines.append(line)
                file.close()
                if not has_sloc_entry:
                    file_lines.append("\nSLOC: " + str(sloc_count))
                file = open(output_file, "w")
                for line in file_lines:
                    file.write(line)
                print("Successfully updated SLOC in output file.")
            except Exception:
                raise
        else:
            print("Specified output file does not exist.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="The desired directory to look in for code.")
    parser.add_argument("--output", help="Will append the number of lines into a file.")
    args = parser.parse_args()
    count_lines_of_code(args.path, args.output)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
