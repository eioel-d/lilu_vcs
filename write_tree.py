from write_object import write_object


def serialize_tree(entries):
    def sort_key(entry):
        name, mode, hex_hash = entry
        key = name.encode()
        if mode == "40000":
            key += b"/"
        return key

    data = b""
    for name, mode, hex_hash in sorted(entries, key=sort_key):
        data += mode.encode() + b" " + name.encode() + b"\0" + bytes.fromhex(hex_hash)

    return data


def write_tree(node, repo):
    entries = []
    for name, value in node.items():
        if isinstance(value, dict):
            sub_hash = write_tree(value, repo)
            entries.append((name, "40000", sub_hash))
        else:
            entries.append((name, value[1], value[0]))
    data = serialize_tree(entries)
    return write_object(data, "tree", repo)
