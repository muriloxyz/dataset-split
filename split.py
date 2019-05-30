import arguments
import dir_utils as utils
import os
import os.path as osp

# convention: args come in (train, val, test) format

def replicate_classes(path, classes, subdirs):
    for subd in subdirs:
        utils.create_dirs(osp.join(path, subd), classes)


def main():
    args = arguments.get_arguments()
    ratio = args.ratio
    # Customized path 
    path = osp.join(os.getcwd(), args.path)

    # Making sure that 3 floats came from cmd line
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"

    data_folders = dict(zip(['train', 'valid', 'test'], ratio))
    classes = utils.list_dirs(path)
    #print(classes)
    utils.create_dirs(path, data_folders.keys()) 
    replicate_classes(path, classes, data_folders)
    #TODO: funct that moves right amount of data to each folder
    #TODO: funct that removes all empty dirs of classes   


if __name__ == '__main__':
    main()
