import os

def list_dirs(path):
    '''
    Given a path, it will return all subdirectorie in it
    except hidden ones.
    '''
    dirs = [fd for fd, _, _ in os.walk(path)]
    dirs = list(filter(lambda x: x[0:3] != './.', dirs))
    dirs = list(filter(lambda x: x != '.', dirs))
    return dirs

def create_dirs(path)
    '''
    Recieves a list of dirs and a path.
    Will create empty dirs inside the path.
    '''
    for d in dirs:
        os.mkdir(d[2:], 0755)

print(list_dirs('.'))
