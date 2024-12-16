# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "hachitool",
# ]
# ///

import hashlib
import importlib.metadata
import platform

import hachitool
from reflex.utils.prerequisites import get_web_dir

web = get_web_dir().absolute()
key_parts = ["reflex-export", platform.system(), platform.machine(), importlib.metadata.version("reflex")]

for lockfile in ["bun.lockb", "package-lock.json"]:
    fp = web / lockfile

    if fp.exists():
        key_parts.append(hashlib.sha256(fp.read_bytes()).hexdigest())

hachitool.set_output("get_key", "-".join(key_parts))
