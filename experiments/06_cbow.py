import json

import train

import common

"""
Аналогично 04_cbow, но размеры эмбеддингов в два раза меньше
"""

name = "06_cbow"

hypers = {
    "query_token_embedding_size": 64,
    "code_token_embedding_size": 64,
}

args = {
    **common.CONSTS,
    **common.DEFAULTS,
    **common.DATA_DIRS_SMALLEST,
    "SAVE_FOLDER": str(common.DIR / "saved" / name),
    "--model": "neuralbowmodel",
    "--run-name": name,
    "--hypers-override": json.dumps(hypers),
}

if __name__ == '__main__':
    train.run(args)
