import train

import common

"""
Тренируем эмбеддинги только на голанге
"""

name = "01_cbow"

args = {
    **common.CONSTS,
    **common.DEFAULTS,
    **common.DATA_DIRS_GO,
    "SAVE_FOLDER": str(common.DIR / "saved" / name),
    "--model": "neuralbowmodel",
    "--run-name": name,
}

if __name__ == '__main__':
    train.run(args)
