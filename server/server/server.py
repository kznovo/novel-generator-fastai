#!/usr/bin/env python3

import os
from pathlib import Path
from fastai.basic_train import load_learner
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def startup():
    global learner
    model_path = Path(os.environ.get("MODEL_PATH", "/tmp/edogawa.pkl"))
    learner = load_learner(path=model_path.parent, file=model_path.name)


async def predict(request):
    string = request.query_params.get("string", "")
    n_words = int(request.query_params.get("n_words", 50))
    preds = learner.predict(string, n_words)
    trimmed = preds.replace(" ", "").replace("xxbos", "")
    return PlainTextResponse(trimmed)


starlette_kwargs = {"routes": [Route("/", predict)], "on_startup": [startup]}
