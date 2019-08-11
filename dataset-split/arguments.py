import argparse

def get_arguments():
    help_str = "Splits your dataset intro train-test-validate subfolders!"
    parser = argparse.ArgumentParser(description=help_str)
    parser.add_argument("path", type=str)
    parser.add_argument("-r", "--ratio", nargs='+', default=[.6,.2,.2], type=float)
    parser.add_argument("-c", "--copy", action='store_true') 
    parser.add_argument("-ns", "--noshuffle", action='store_true')
    # Return it as a dict
    return parser.parse_args()

