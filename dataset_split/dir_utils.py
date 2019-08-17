import os
import os.path as osp
import shutil as sh

def move_files(origin, dest, items):
    '''
    Given 2 paths, origin and (dest)iny, and a list of items,
    it will MOVE all listed files of origin to the specified
    destination.
    '''
    for item in items:
        origin_file = osp.join(origin, item)
        sh.move(origin_file, dest)

def copy_files(origin, dest, items):
    '''
    Given 2 paths, origin and (dest)iny, and a list of items,
    it will COPY all listed files of origin to the specified
    destination.
    '''
    for item in items:
        origin_file = osp.join(origin, item)
        sh.copy2(origin_file, dest)

def list_dirs(path):
    '''
    Given a path, it will return all subdirectories in it
    (except hidden ones).
    '''
    dirs = [f for f in os.listdir(path) if osp.isdir(osp.join(path, f))]
    #Filter hidden directories
    dirs = list(filter(lambda x: x[0] != '.', dirs))
    return dirs

def create_dirs(path, dirs):
    '''
    Recieves a list of dirs and a path.
    Will create empty dirs inside the path.
    '''
    for d in dirs:
        os.mkdir(osp.join(path, d))

def remove_dirs(path, dirs):
    '''
    Recieves a list of dirs and a path.
    Will remove recursively every listed directories
    inside the path and anything inside them.
    '''
    for d in dirs:
        sh.rmtree(osp.join(path, d))
