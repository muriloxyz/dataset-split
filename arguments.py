import argparse

def get_arguments():
    help_str = "Splits your dataset intro train-test-validate subfolders!"
    parser = argparse.ArgumentParser(description=help_str)
    # Default path is the current folder.
    parser.add_argument("path", type=str)
    parser.add_argument('-r', "--ratio", nargs='+', type=float)
    # Return it as a dict
    return parser.parse_args()

