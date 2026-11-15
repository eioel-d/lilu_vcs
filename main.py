from init import init
from create_object import create_object
from write_commit import write_commit
from write_tree import write_tree
from os.path import exists, abspath

import sys


def main():
    repo = {
        "lilu": abspath(".lilu") + "/",
        "objects": abspath(".lilu/objects") + "/",
        "refs": abspath(".lilu/refs") + "/",
        "refs_heads": abspath(".lilu/refs/heads") + "/",
        "head": abspath(".lilu/HEAD"),
    }

    match sys.argv[1]:
        case "init":
            init()
            return
        case "add":
            if not exists(".lilu"):
                print("Repository not initialized, please initialize first")
                return

            if not sys.argv[2]:
                print("Didn't provide files to track")
                return
            create_object(sys.argv[2], repo)
        case "commit":
            if not exists(".lilu"):
                print("Repository not initialized, please initialize first")
                return

            if not sys.argv[2]:
                print("Commit message was not provided")
                return
            tree_hash = write_tree(create_object(".", repo), repo)
            write_commit(sys.argv[2], tree_hash, repo)
        case _:
            print(f"{sys.argv[1]} is an unknown command")


if __name__ == "__main__":
    main()
