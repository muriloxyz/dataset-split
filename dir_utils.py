import os
import os.path

def list_dirs(path):
    '''
    Given a path, it will return all subdirectorie in it
    except hidden ones.
    '''
    os.chdir(os.path.join(os.getcwd(), path))
    dirs = [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]
    os.chdir(os.path.join(os.getcwd(), '..'))
    #Filter hidden directories
    return list(filter(lambda x: x[0] != '.', dirs))

def create_dirs(dirs):
    '''
    Recieves a list of dirs and a path.
    Will create empty dirs inside the path.
    '''
    for d in dirs:
        os.mkdir(d)

