#!/usr/bin/env python

import os
import os.path as osp
import random
from math import floor
import dataset_split.dir_utils as utils

#CONVENTION: args come in (train, test, val) format 
COPY_FOLDER = '_split_'

def replicate_classes(path, classes, subdirs):
    '''
    Will create all classes (dirs) inside every
    subdir found in path. 
    '''
    for subd in subdirs:
        utils.create_dirs(osp.join(path, subd), classes)

def calculate_splits(items, folders, shuffle_enabled):
    '''
    With a list of files (items) and numbers for folders ratios,
    shuffles (if requested) the files and decides their final
    folder in the split.
    '''
    #If requested, generates a random seed and shuffle items
    if shuffle_enabled:
        random.seed = os.urandom(49)
        random.shuffle(items)
    n = len(items)
    #Calculating where the list will be sliced
    train_limit = round(folders['train'] * n)
    test_limit = train_limit + floor(folders['test'] * n)
    #Sliced list for every subset
    split = {'train': items[:train_limit],
             'test': items[train_limit:test_limit],
             'valid': items[test_limit:]
            }
    return split

def move_data(orig_path, dest_path, splits, subd):
    '''
    With the split already decided, this function
    moves the files to their respective destination.
    '''
    for d in splits.keys():
        origin = osp.join(orig_path, subd)
        dest = osp.join(dest_path, d, subd)
        utils.move_files(origin, dest, splits[d])

def copy_data(orig_path, dest_path, splits, subd):
    '''
    With the split already decided, this function
    copies the files to their respective destination.
    '''
    for d in splits.keys():
        origin = osp.join(orig_path, subd)
        dest = osp.join(dest_path, d, subd)
        utils.copy_files(origin, dest, splits[d])

def split_data(orig_path, dest_path, classes, new_folders, 
               copy_enabled, shuffle_enabled):
    '''
    Calculates the split for traint-valid-test dirs
    and moves the right amount of files.
    '''
    for subd in classes:
        temp_path = osp.join(orig_path, subd)
        items = [f for f in os.listdir(temp_path)]
        splits = calculate_splits(items, new_folders, shuffle_enabled)
        if copy_enabled:
            copy_data(orig_path, dest_path, splits, subd)
        else:
            move_data(orig_path, dest_path, splits, subd)

def split(ratio, orig_path, copy_enabled, shuffle_enabled=True):
    '''
    Splits a dataset after reading it's path
    through cmd line and the desired ratio.
    Will create three new folders: train, test, valid
    '''
    # Making sure that 3 floats came from cmd line
    assert len(ratio) == 3, "Ratio didn't get 3 parameters"
    assert (0.99 <= sum(ratio) <= 1.01), "Ratio doesn't sum up to 1"
    data_folders = dict(zip(['train', 'test', 'valid'], ratio))
    dest_path = orig_path
    classes = utils.list_dirs(orig_path) 
    if copy_enabled:
        dest_path = osp.join(orig_path, COPY_FOLDER)
        os.mkdir(dest_path)
    utils.create_dirs(dest_path, data_folders.keys())
    replicate_classes(dest_path, classes, data_folders)
    split_data(orig_path, dest_path, classes, data_folders, copy_enabled, shuffle_enabled)
    # If copy is enabled, remove the original dataset folders
    if not copy_enabled:
        utils.remove_dirs(orig_path, classes)

def main():
    args = arguments.get_arguments()
    path = osp.join(os.getcwd(), args.path)
    split(args.ratio, path, args.copy, not args.noshuffle)

if __name__ == '__main__':
    main()
