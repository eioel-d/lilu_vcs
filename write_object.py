from hashlib import sha1
from zlib import compress
from os import path, makedirs


def write_object(data, content_type: str, repo):
    data = f"{content_type} {len(data)}\0".encode() + data
    hex_code = sha1(data).hexdigest()
    folder_path = f"{repo['objects']}/{hex_code[:2]}"
    file_path = hex_code[2:]
    object_path = f"{folder_path}/{file_path}"
    if not path.exists(object_path):
        makedirs(folder_path, exist_ok=True)
        with open(object_path, "wb") as f:
            f.write(compress(data))
    return hex_code
