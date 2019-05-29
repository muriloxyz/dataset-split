import arguments
import dir_utils as utils



def main():
    args = arguments.get_arguments()
    split_ratio = calculate_split(args)
    print(split_ratio)
    #classes = utils.list_dirs(args.path)
    #TODO: funct that creates train-test-val folders and classes inside
    #TODO: funct that moves right amount of data to each folder
    

def calculate_split(args):
    ratio_sum = args.train + args.test + args.val
    if 0 <= ratio_sum <= 100: 
        if ratio_sum == 100:
            train_ratio = args.train/100
            test_ratio = args.test/100
            val_ratio = args.val/100
        elif ratio_sum == 0:
            train_ratio = .6
            test_ratio = .2
            val_ratio = .2
        else:
            train_ratio = args.train/100 if args.train != 0 else (100 - ratio_sum)/100
            test_ratio = args.test/100 if args.test != 0 else (100 - ratio_sum)/100
            val_ratio = args.val/100 if args.val != 0 else (100 - ratio_sum)/100
    else:
        print("Invalid combination of arguments!")
        exit(1)
    return train_ratio, test_ratio, val_ratio


if __name__ == '__main__':
    main()
