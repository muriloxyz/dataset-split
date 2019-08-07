import pytest
import os
import os.path as osp
import shutil as sh
import split as sp

COPY_FOLDER = '_split_'
THIS_PATH = osp.join(os.getcwd(), 'test')
SAFE_PATH = osp.join(THIS_PATH, 'test-dataset')
TEST_PATH = osp.join(THIS_PATH, 'test-dataset-exec')
TEST_COPY_PATH = osp.join(TEST_PATH, COPY_FOLDER)
GENERATED_DIRS = ['test', 'valid', 'train']
RATIO = (.6, .2, .2) 


@pytest.fixture(autouse=True)
def clean_mess():
    #Before each function creates a new test folder
    sh.copytree(SAFE_PATH, TEST_PATH)
    yield
    #After each function delete the test folder
    sh.rmtree(TEST_PATH)

def list_dirs(path):
    return [d for d in os.listdir(path) if osp.isdir(osp.join(path, d))]

def list_items(path):
    # List all items inside the dataset (for each class)
    classes = list_dirs(path)
    items = [os.listdir(osp.join(path, c)) for c in classes]
    return dict(zip(classes, items))

def quantities_check(before, after):
    pass

def test_split_copy():
    # Tests split when copying files
    original_items = list_items(TEST_PATH)
    sp.split(RATIO, TEST_PATH, True)
    # Check: Copy directory created
    assert COPY_FOLDER in os.listdir(TEST_PATH)
    # Check: The number of directories increased by one (split folder)
    assert len(list_dirs(TEST_PATH)) == len(original_items) + 1
    # Check: Check if split dir has the generated test/train/valid.
    assert set(list_dirs(osp.join(TEST_PATH, COPY_FOLDER))) == set(GENERATED_DIRS) 
    #after_split = [list_items(d) for d in os.list_dirs(osp.join(TEST_PATH, COPY_FOLDER))]
    #assert after_split


def test_split_move():
    # Tests split when moving files
    original_items = list_items(TEST_PATH)
    sp.split(RATIO, TEST_PATH, False)
    assert set(list_dirs(TEST_PATH)) == set(GENERATED_DIRS)

