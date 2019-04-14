import re
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
import MeCab
from fastai.text.transform import BaseTokenizer
from fastai.basic_train import load_learner
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse

if __name__ == "__main__":

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

    learner = load_learner(path="/app", file="model.pkl")
    app = Starlette()

    @app.route("/")
    async def index(request):
        string = request.query_params["string"]
        n_words = request.query_params["n_words"]
        preds = learner.predict(string, int(n_words))
        trimmed = preds.replace(" ", "").replace("xxbos", "")
        return PlainTextResponse(trimmed)

    cfg_mapping = {"bind": "0.0.0.0:8000", "access_log_target": "-"}
    config = Config.from_mapping(cfg_mapping)
    asyncio.run(serve(app, config))

