from datetime import datetime
from os import path
from write_object import write_object


def write_commit(message, tree_hash, repo):
    t = datetime.now()
    date = str(int(t.timestamp()))
    timezone = t.astimezone().strftime("%z")

    user = {
        "name": "eioel",
        "email": "eioeldagnachew@gmail.com",
        "date": date,
        "timezone": timezone,
    }
    with open(repo["head"], "r") as f:
        object_path = repo["lilu"] + "/" + f.read().split("ref: ", 1)[1].rstrip("\n")
    parent = ""
    if path.exists(object_path):
        with open(object_path, "r") as f:
            parent = f.read().rstrip("\n")
    author = (
        f"author {user['name']} <{user['email']}> {user['date']} {user['timezone']}\n"
    )
    committer = f"committer {user['name']} <{user['email']}> {user['date']} {user['timezone']}\n"
    parent_hash = "parent " + parent + "\n"
    content = f"tree {tree_hash}\n{parent_hash if parent else ''}{author}{committer}\n{message}\n".encode()

    commit = write_object(content, "commit", repo)
    with open(object_path, "w") as f:
        f.write(commit + "\n")

    return commit
