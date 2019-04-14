FROM fastai-edogawa-base:latest
COPY . .
EXPOSE 8000
ENTRYPOINT ["python", "server.py"]
