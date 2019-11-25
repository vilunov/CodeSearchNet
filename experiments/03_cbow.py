import json

import train

import common

"""
эмбеддинги в 8 раз больше бейзлайна
на go и javascript
батчи тоже в 8 раз больше 
"""

name = "03_cbow"

hypers = {
    "batch_size": 1000,
    "query_token_embedding_size": 1024,
    "code_token_embedding_size": 1024,
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
