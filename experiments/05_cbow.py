import json

import train

import common

"""
Аналогично 04_cbow, но размеры эмбеддингов в два раза больше
"""

name = "05_cbow"

hypers = {
    "query_token_embedding_size": 256,
    "code_token_embedding_size": 256,
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
