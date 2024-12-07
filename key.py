import hashlib
import importlib.metadata
import platform

import github_action_utils as gha
from reflex.utils.prerequisites import get_web_dir


web = get_web_dir().absolute()
key_parts = ["reflex-export", platform.system(), platform.machine(), "reflex", importlib.metadata.version("reflex")]


for lockfile in ["bun.lockb", "package-lock.json"]:
    fp = web / lockfile

    if fp.exists():
        key_parts.append(hashlib.sha256(fp.read_bytes()).hexdigest())

gha.set_output("key", "-".join(key_parts))