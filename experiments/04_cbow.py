import train

import common

"""
только на на go и javascript 
"""

name = "04_cbow"

args = {
    **common.CONSTS,
    **common.DEFAULTS,
    **common.DATA_DIRS_SMALLEST,
    "SAVE_FOLDER": str(common.DIR / "saved" / name),
    "--model": "neuralbowmodel",
    "--run-name": name,
}

if __name__ == '__main__':
    train.run(args)
