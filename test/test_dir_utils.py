import pytest
import os
import os.path as osp
import shutil as sh

# Adding parent directory in order to
# import dir_utils
import sys
sys.path.append("..")
import dir_utils

SAFE_FOLDER = osp.join(os.getcwd(), 'test-directories')
TEST_PATH = osp.join(os.getcwd(), 'test-directories-exec')
TEST_DIRS = ['OMG', 'ROFL', 'XOXO', '.SNEAKY']

@pytest.fixture(autouse=True)
def clean_mess():
    #Before each function creates a new test folder
    sh.copytree(SAFE_FOLDER, TEST_PATH)
    yield
    #After each function delete the test folder
    sh.rmtree(TEST_PATH)

def test_list_dirs():
    expected1 = {'Apple', 'Pineapple', 'Orange'}
    expected2 = {'Spaghetti', 'Steak', 'Rice'}
    listed_dirs1 = dir_utils.list_dirs(osp.join(TEST_PATH, 'folder1'))
    listed_dirs2 = dir_utils.list_dirs(osp.join(TEST_PATH, 'folder2'))
    assert len(expected1) == len(listed_dirs1)
    assert len(expected2) == len(listed_dirs2)
    assert expected1 == set(listed_dirs1)
    assert expected2 == set(listed_dirs2)

def test_create_dirs():
    dir_utils.create_dirs(TEST_PATH, TEST_DIRS)
    listed_dirs = [d for d in os.listdir(TEST_PATH)]
    expected = set(TEST_DIRS).union({'folder1', 'folder2'})
    assert len(expected) == len(listed_dirs)
    assert expected == set(listed_dirs)
