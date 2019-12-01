http://kznovo.github.io/novel-generator-fastai

# Development
### Model Development:
- [Open in Google Colab Notebook](https://colab.research.google.com/github/kznovo/novel-generator-fastai/blob/master/dev/model_training.ipynb)
### Server Development: 

```console
scripts/dev_deploy
```

# Available scripts:
### `scripts/dev_model`
- start model development container (jupyter notebook) locally

### `scripts/dev_deploy [modelpath]`
- start model server development container

### `scripts/deploy [modelpath]`
- start model server container (serves model at `modelpath`; default `modelpath=./model.pkl`)
