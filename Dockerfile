FROM python:3.7-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  cmake \
  swig \
  mecab \
  libmecab-dev \
  mecab-ipadic-utf8 &&\
  rm -rf /var/lib/apt/lists/*
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5001
ENV MODEL_PATH=/app/model.pkl
ENTRYPOINT ["python", "server.py"]
