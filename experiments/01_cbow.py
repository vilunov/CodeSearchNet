import train

import common

args = {
    **common.CONSTS,
    **common.DEFAULTS,
    **common.DATA_DIRS_GO,
    "SAVE_FOLDER": "saved/00_cbow",
    "--model": "neuralbowmodel",
    "--run-name": "00_cbow",
}

if __name__ == '__main__':
    train.run(args)
