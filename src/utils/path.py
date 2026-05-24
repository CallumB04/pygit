import os

# build path inside the repo
# *path allows for one or multiple arguements
def repo_path(repo, *path):
    return os.path.join(repo.gitdir, *path)

# return full path to a file inside the repo
# if mkdir=True, creates parent directories if they dont exist
def repo_file(repo, *path, mkdir=False):

    # *path[:-1] -> parent directory path
    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)

# return full path to a directory inside the repo
# if mkdir=True, creates directory if doesnt exist
def repo_dir(repo, *path, mkdir=False):
    path = repo_path(repo, *path)

    # check if directory exists and return it
    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception(f"Not a directory {path}")

    # if directory doesnt exist and mkdir=True, create and return path
    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None