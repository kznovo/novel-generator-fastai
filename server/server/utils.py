#!/usr/bin/env python3

import typing
import natto
from fastai.text.transform import BaseTokenizer
from fastai.basic_train import load_learner


nm = natto.MeCab()


class MeCabTokenizer(BaseTokenizer):
    def __init__(self, lang: str) -> None:
        self.lang = "ja"

    def add_special_cases(self, toks: typing.Collection[str]) -> None:
        pass

    def tokenizer(self, raw_sentence: str) -> typing.List[str]:
        return [node.surface for node in nm.parse(raw_sentence, as_nodes=True)]
