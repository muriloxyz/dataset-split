import argparse

def get_arguments():
    help_str = "Splits your dataset intro train-test-validate subfolders!"
    parser = argparse.ArgumentParser(description=help_str)
    # Default path is the current folder.
    parser.add_argument("path", type=str)
    parser.add_argument('-T', "--train", type=float, default=None)
    parser.add_argument('-t', "--test", type=float, default=None)
    parser.add_argument('-V', "--val", type=float, default=None)
    # Return it as a dict
    return vars(parser.parse_args())

