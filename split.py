import arguments
import dir_utils as utils



def main():
    args = arguments.get_arguments()
    ratio = args.ratio
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"
    #print(ratio)
    #classes = utils.list_dirs(args.path)
    #TODO: funct that creates train-test-val folders and classes inside
    #TODO: funct that moves right amount of data to each folder
    


if __name__ == '__main__':
    main()
