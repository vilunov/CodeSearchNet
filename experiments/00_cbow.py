import train

import common

name = "00_cbow"

args = {
    **common.CONSTS,
    **common.DEFAULTS,
    **common.DATA_DIRS_LARGEST,
    "SAVE_FOLDER": str(common.DIR / "saved" / name),
    "--model": "neuralbowmodel",
    "--run-name": name,
}

if __name__ == '__main__':
    train.run(args)
