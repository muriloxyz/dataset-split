import arguments
import dir_utils as utils
import os
import os.path as osp
from random import shuffle
from math import ceil, floor

# convention: args come in (train, val, test) format

def replicate_classes(path, classes, subdirs):
    '''
    Will create all classes (dirs) inside every
    subdir found in path. 
    '''
    for subd in subdirs:
        utils.create_dirs(osp.join(path, subd), classes)

def calculate_splits(items, folders):
    '''
    With a list of files (items) and numbers for folders ratios,
    shuffles (if requested) the files and decides their final
    folder in the split.
    '''
    shuffle(items)
    n = len(items)
    #Calculating where the list will be sliced
    train_limit = ceil(folders['train'] * n)
    test_limit = train_limit + floor(folders['test'] * n)
    #Sliced list for every subset
    split = {'train': items[:train_limit],
             'valid': items[train_limit:test_limit],
             'test': items[test_limit:]
            }
    return split

def move_data(path, splits, subd):
    '''
    With the split already decided, this function
    moves the files to their respective destination.
    '''
    for d in splits.keys():
        origin = osp.join(path, subd)
        dest = osp.join(path, d, subd)
        utils.move_files(origin, dest, splits[d])

def split_data(path, classes, new_folders):
    '''
    Calculates the split for traint-valid-test dirs
    and moves the right amount of files.
    '''
    for subd in classes:
        temp_path = osp.join(path, subd)
        items = [f for f in os.listdir(temp_path)]
        splits = calculate_splits(items, new_folders)
        move_data(path, splits, subd)

def main():
    '''
    To be added
    '''
    args = arguments.get_arguments()
    ratio = args.ratio
    # Customized path 
    path = osp.join(os.getcwd(), args.path)

    # Making sure that 3 floats came from cmd line
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"
    assert sum(ratio) == 1, "Ratio doesn't sum up to 1"

    data_folders = dict(zip(['train', 'valid', 'test'], ratio))
    classes = utils.list_dirs(path)
    utils.create_dirs(path, data_folders.keys()) 
    replicate_classes(path, classes, data_folders)
    split_data(path, classes, data_folders)
    utils.remove_dirs(path, classes)


if __name__ == '__main__':
    main()
