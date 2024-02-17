import sys
import os
import argparse
import genanki

def create_card(word):
    pass

def convert(files):
    for file in files:
        try:
            with open(file, 'r') as f:
                for line in f:
                    content = f.read()
                    create_card(line.lstrip().rstrip())
        except FileNotFoundError:
            print(f"Error: File '{file} not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Exception {e} occurred.")
            sys.exit(1)

    print('Converted!')

def main():
    parser = argparse.ArgumentParser(description="Convert words in a given text document into anki cards.")
    parser.add_argument('-f', '--files', nargs='+', help="File(s) to be converted into an anki cards.", required=True)

    args = parser.parse_args()

    files = args.files

    def abs_path(file):
        if not os.path.isabs(file):
            return os.path.abspath(file)
        return file

    convert(list(map(abs_path, files)))

if __name__ == "__main__":
    main()