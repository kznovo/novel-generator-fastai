#!/usr/bin/env python3

import uvicorn
from starlette.applications import Starlette
from server import starlette_kwargs

if __name__ == "__main__":
    from utils import MeCabTokenizer

    app = Starlette(**starlette_kwargs)
    uvicorn.run(app, host="127.0.0.1", port=5001, log_level="info")
