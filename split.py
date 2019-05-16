import arguments
import dir_utils as utils



def main():
    args = arguments.get_arguments()
    split_ratio = calculate_split(args)
    classes = utils.list_dirs(args.path)
    #TODO: funct that creates train-test-val folders and classes inside
    #TODO: funct that moves right amount of data to each folder
    

def calculate_split(args):
    ratio_sum = args.train + args.test + args.val
    if 0 <= ratio_sum <= 100: 
        #TODO: Decide what to do w/
        #missing args
    else:
        print("Invalid combination of arguments!")
        exit(1)
    
if __name__ == '__main__':
    main()
