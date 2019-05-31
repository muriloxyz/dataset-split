import arguments
import dir_utils as utils
import os
import os.path as osp
from random import shuffle
from math import ceil, floor

# convention: args come in (train, val, test) format

def replicate_classes(path, classes, subdirs):
    for subd in subdirs:
        utils.create_dirs(osp.join(path, subd), classes)

def calculate_splits(items, folders):
    shuffle(items)
    n = len(items)
    train_limit = ceil(folders['train'] * n)
    test_limit = train_limit + floor(folders['test'] * n)
    split = {'train': items[:train_limit],
             'valid': items[train_limit:test_limit],
             'test': items[test_limit:]
            }
    return split

def move_data(path, splits, subd):
    for d in splits.keys():
        origin = osp.join(path, subd)
        dest = osp.join(path, d, subd)
        utils.move_files(origin, dest, splits[d])

def split_data(path, classes, new_folders):
    for subd in classes:
        temp_path = osp.join(path, subd)
        items = [f for f in os.listdir(temp_path)]
        splits = calculate_splits(items, new_folders)
        move_data(path, splits, subd)

def main():
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
