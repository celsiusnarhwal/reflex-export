import hashlib
import importlib.metadata
import platform

import hachitool
import typer
from reflex.utils.prerequisites import get_web_dir


app = typer.Typer()


@app.command("get-web")
def get_web():
    hachitool.set_output("get_web", get_web_dir().absolute())

@app.command("get-get_key")
def get_key():
    web = get_web_dir().absolute()
    key_parts = ["reflex-export", platform.system(), platform.machine(), importlib.metadata.version("reflex")]

    for lockfile in ["bun.lockb", "package-lock.json"]:
        fp = web / lockfile

        if fp.exists():
            key_parts.append(hashlib.sha256(fp.read_bytes()).hexdigest())

    hachitool.set_output("key", "-".join(key_parts))
