import stat
import os
from write_object import write_object


def create_object(file_name, repo):
    folder_path = repo["refs_heads"]
    HEAD = repo["head"]
    if not os.path.exists(HEAD):
        with open(HEAD, "w") as f:
            f.write(f"ref: {os.path.relpath(folder_path).split('/', 1)[1]}/main\n")
    entries = {}
    if os.path.isdir(file_name):
        for file in sorted(os.listdir(file_name)):
            full_path = os.path.join(file_name, file)
            if file == ".lilu" or file == ".git":
                continue
            entry = create_object(full_path, repo)

            if entry:
                entries[file] = entry
        return entries

    with open(file_name, "rb") as f:
        content = f.read()

    return (
        write_object(content, "blob", repo),
        "100755" if (os.stat(file_name).st_mode & stat.S_IXUSR) else "100644",
    )
