import arguments
import dir_utils as utils
import os
import os.path

# convention: args come in train - val - test

def main():
    args = arguments.get_arguments()
    path = args.path
    ratio = args.ratio
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"
    folders = dict(zip(['train', 'valid', 'test'], ratio))
    classes = utils.list_dirs(path)
    print(folders)
    print("Classes: {}".format(classes))
    #TODO: funct that creates train-test-val folders and classes inside
    #TODO: funct that moves right amount of data to each folder
    


if __name__ == '__main__':
    main()
