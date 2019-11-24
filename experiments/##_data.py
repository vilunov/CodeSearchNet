from dpu_utils.utils import RichPath

from metadata import MetadataLoader
from models.nbow_model import NeuralBoWModel

PATHS = {
    "python": "../resources/data/python/final/jsonl/train",
    "javascript": "../resources/data/javascript/final/jsonl/train",
    "java": "../resources/data/java/final/jsonl/train",
    "php": "../resources/data/php/final/jsonl/train",
    "ruby": "../resources/data/ruby/final/jsonl/train",
    "go": "../resources/data/go/final/jsonl/train",
}

def main():
    paths = [RichPath.create(i) for i in PATHS.values()]
    model_class = NeuralBoWModel
    loader = MetadataLoader(
        model_class.query_encoder_type, model_class.code_encoder_type, model_class.get_default_hyperparameters())
    loader.load_parallel(paths)

    code_data = loader.raw_code_language_metadata_lists
    for language, metadata in code_data.items():
        tokens = sum(sum(i["token_counter"].values()) for i in metadata)
        print(f"{language}: {tokens}")


if __name__ == '__main__':
    main()
