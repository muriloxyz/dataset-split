import argparse

def get_arguments():
    help_str = "Splits your dataset intro train-test-validate subfolders!"
    parser = argparse.ArgumentParser(description=help_str)
    # Default path is the current folder.
    parser.add_argument("path", type=str)
    parser.add_argument('-T', "--train", type=int, default=0)
    parser.add_argument('-t', "--test", type=int, default=0)
    parser.add_argument('-V', "--val", type=int, default=0)
    # Return it as a dict
    return parser.parse_args()

