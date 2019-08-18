import pytest
import os
import os.path as osp
import shutil as sh
import dataset_split.dir_utils as dir_utils

THIS_PATH = osp.join(os.getcwd(), 'dataset_split', 'test')
SAFE_PATH = osp.join(THIS_PATH, 'test-utils')
TEST_PATH = osp.join(THIS_PATH, 'test-utils-exec')
TEST_DIRS = ['OMG', 'ROFL', 'XOXO', '.SNEAKY']
ORIGINAL_DIRS = ['folder1', 'folder2']

@pytest.fixture(autouse=True)
def clean_mess():
    #Before each function creates a new test folder
    sh.copytree(SAFE_PATH, TEST_PATH)
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
    #Creating dumming directories
    dir_utils.create_dirs(TEST_PATH, TEST_DIRS)
    #Listing every dir
    listed_dirs = [d for d in os.listdir(TEST_PATH)]
    expected = set(TEST_DIRS).union(set(ORIGINAL_DIRS))
    assert len(expected) == len(listed_dirs)
    assert expected == set(listed_dirs)

def test_remove_dirs():
    # Creating dummie directories
    for d in TEST_DIRS:
        os.mkdir(osp.join(TEST_PATH, d))
    #Removing them
    dir_utils.remove_dirs(TEST_PATH, TEST_DIRS)
    #Listing and testing
    listed_dirs = [d for d in os.listdir(TEST_PATH)]
    assert  set(ORIGINAL_DIRS) == set(listed_dirs)

