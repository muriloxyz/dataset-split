import pytest
import os
import os.path as osp
import shutil as sh
import dir_utils

COPY_FOLDER = '_split_'
THIS_PATH = osp.join(os.getcwd(), 'test')
SAFE_PATH = osp.join(THIS_PATH, 'test-dataset')
TEST_PATH = osp.join(THIS_PATH, 'test-dataset-exec')
TEST_COPY_PATH = osp.join(TEST_PATH, COPY_FOLDER)
RATIO = (.6, .2, .2) 


@pytest.fixture(autouse=True)
def clean_mess():
    #Before each function creates a new test folder
    sh.copytree(SAFE_PATH, TEST_PATH)
    yield
    #After each function delete the test folder
    sh.rmtree(TEST_PATH)

def list_items():
    # List all items inside the dataset (orders by class)
    classes = [c for c in os.listdir(TEST_PATH) if osp.isdir(osp.join(TEST_PATH, c))]
    items = [os.listdir(osp.join(TEST_PATH, c)) for c in classes]
    return dict(zip(classes, items))


def test_split_copy():
    # Tests split when copying files
    pass

def test_split_move():
    # Tests split when moving files
    pass
