import pathlib
DIR = pathlib.Path(__file__).parent

DATA_DIRS_LARGEST = {
    "TRAIN_DATA_PATH": str(DIR / "data_dirs/largest/train.txt"),
    "VALID_DATA_PATH": str(DIR / "data_dirs/largest/valid.txt"),
    "TEST_DATA_PATH": str(DIR / "data_dirs/largest/test.txt"),
}

DATA_DIRS_SMALLEST = {
    "TRAIN_DATA_PATH": str(DIR / "data_dirs/smallest/train.txt"),
    "VALID_DATA_PATH": str(DIR / "data_dirs/smallest/valid.txt"),
    "TEST_DATA_PATH": str(DIR / "data_dirs/smallest/test.txt"),
}

DATA_DIRS_GO = {
    "TRAIN_DATA_PATH": str(DIR / "data_dirs/go/train.txt"),
    "VALID_DATA_PATH": str(DIR / "data_dirs/go/valid.txt"),
    "TEST_DATA_PATH": str(DIR / "data_dirs/go/test.txt"),
}

CONSTS = {
    "--quiet": False,
    "--dryrun": False,
    "--testrun": False,
    "--sequential": False,
    "--debug": False,
}

DEFAULTS = {
    "--max-num-epochs": "300",
    "--test-batch-size": "100",
    "--distance-metric": "cosine",
}