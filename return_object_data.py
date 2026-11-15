import sys
from zlib import decompress


def read_object(hex_code):
    path = hex_code
    with open(path, "rb") as f:
        raw = decompress(f.read())
    header, content = raw.split(b"\0", 1)
    obj_type, size = header.decode().split(" ")
    return obj_type, content


def parse_tree(content):
    entries = []
    pos = 0
    while pos < len(content):
        space = content.index(b" ", pos)
        mode = content[pos:space].decode()
        null = content.index(b"\0", space)
        name = content[space + 1 : null].decode()
        hash_hex = content[null + 1 : null + 21].hex()
        entries.append((mode, name, hash_hex))
        pos = null + 21
    return entries


if __name__ == "__main__":
    obj_type, content = read_object(sys.argv[1])
    if obj_type == "tree":
        for mode, name, hash_hex in parse_tree(content):
            kind = "tree" if mode == "40000" else "blob"
            print(f"{mode.zfill(6)} {kind} {hash_hex}\t{name}")
    else:
        print(content.decode())
