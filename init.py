from os import makedirs, path


def init():
    repo_dir = ".lilu"
    objects_dir = path.join(repo_dir, "objects")
    refs_dir = path.join(repo_dir, "refs")

    makedirs(repo_dir, exist_ok=True)
    makedirs(objects_dir, exist_ok=True)
    makedirs(refs_dir + "/heads", exist_ok=True)

    print(f"Repository initialized in {path.abspath('lilu')}")
