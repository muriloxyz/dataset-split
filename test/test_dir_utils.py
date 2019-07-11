import pytest
import os
import os.path as osp
import shutil as sh

# Adding parent directory in order to
# import dir_utils
import sys
sys.path.append("..")
import dir_utils

TEST_PATH = osp.join(os.getcwd())
TEST_DIRS = ['OMG', 'ROFL', 'XOXO', '.SNEAKY']

def test_list_dirs():
    expected1 = {'Apple', 'Pineapple', 'Orange'}
    expected2 = {'Spaghetti', 'Steak', 'Rice'}
    path = osp.join(TEST_PATH, 'test-directories')
    listed_dirs1 = dir_utils.list_dirs(osp.join(path, 'folder1'))
    listed_dirs2 = dir_utils.list_dirs(osp.join(path, 'folder2'))
    assert len(expected1) == len(listed_dirs1)
    assert len(expected2) == len(listed_dirs2)
    assert expected1 == set(listed_dirs1)
    assert expected2 == set(listed_dirs2)

def test_create_dirs():
    path = osp.join(TEST_PATH, 'test-directories')
    dir_utils.create_dirs(path, TEST_DIRS)
    listed_dirs = [d for d in os.listdir(path)]
    expected = set(TEST_DIRS).union({'folder1', 'folder2'})
    assert len(expected) == len(listed_dirs)
    assert expected == set(listed_dirs)


