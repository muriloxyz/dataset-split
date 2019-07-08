import arguments
import dir_utils as utils
import os
import os.path as osp
from random import shuffle
from math import ceil, floor

# convention: args come in (train, test, val) format

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
             'test': items[train_limit:test_limit],
             'valid': items[test_limit:]
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

def copy_data(path, splits, subd):
    '''
    With the split already decided, this function
    copies the files to their respective destination.
    '''
    for d in splits.keys():
        origin = osp.join(path, subd)
        dest = osp.join(path, d, subd)
        utils.copy_files(origin, dest, splits[d])

def split_data(path, classes, new_folders, copy_enabled):
    '''
    Calculates the split for traint-valid-test dirs
    and moves the right amount of files.
    '''
    for subd in classes:
        temp_path = osp.join(path, subd)
        items = [f for f in os.listdir(temp_path)]
        splits = calculate_splits(items, new_folders)
        if copy_enabled:
            move_data(path, splits, subd)
        else:
            copy_data(path, splits, subd)

def split(ratio, path, copy):
    '''
    Splits a dataset after reading it's path
    through cmd line and the desired ratio.
    Will create three new folders: train, test, valid
    '''
    # Making sure that 3 floats came from cmd line
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"
    assert sum(ratio) == 1, "Ratio doesn't sum up to 1"
    data_folders = dict(zip(['train', 'test', 'valid'], ratio))
    classes = utils.list_dirs(path)
    utils.create_dirs(path, data_folders.keys()) 
    replicate_classes(path, classes, data_folders)
    split_data(path, classes, data_folders, copy)
    if not copy:
        utils.remove_dirs(path, classes)

def main():
    args = arguments.get_arguments()
    path = osp.join(os.getcwd(), args.path)
    split(args.ratio, path, args.copy)

if __name__ == '__main__':
    main()
