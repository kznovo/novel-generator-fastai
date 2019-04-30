import re
import os
from pathlib import Path
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
import MeCab
from fastai.text.transform import BaseTokenizer
from fastai.basic_train import load_learner
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware

tagger = MeCab.Tagger("-Owakati")


class MeCabTokenizer(BaseTokenizer):
    def __init__(self, lang: str):
        self.lang = "ja"

    def add_special_cases(self, toks):
        pass

    def tokenizer(self, raw_sentence):
        result = tagger.parse(raw_sentence)
        words = result.split()
        if len(words) == 0:
            return []
        if words[-1] == "\n":
            words = words[:-1]
        return words


if __name__ == "__main__":
    model_path = Path(os.environ["MODEL_PATH"])
    learner = load_learner(path=model_path.parent, file=model_path.name)
    app = Starlette()
    app.add_middleware(CORSMiddleware, allow_origins=["*"])

    @app.route("/")
    async def index(request):
        string = request.query_params["string"]
        n_words = request.query_params["n_words"]
        preds = learner.predict(string, int(n_words))
        trimmed = preds.replace(" ", "").replace("xxbos", "")
        return PlainTextResponse(trimmed)

    cfg_mapping = {"bind": "0.0.0.0:5001", "access_log_target": "-"}
    config = Config.from_mapping(cfg_mapping)
    asyncio.run(serve(app, config))

