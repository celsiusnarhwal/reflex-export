# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "hachitool",
# ]
# ///

import hachitool
from reflex.config import get_config
from reflex.utils.prerequisites import get_web_dir

hachitool.set_output(web=get_web_dir().absolute())