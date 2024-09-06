FROM python:3.10.6-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY api api/

COPY setup.py setup.py


RUN apt-get update
RUN apt-get install \
  'ffmpeg'\
  'libsm6'\
  'libxext6'  -y

RUN pip install -e .

COPY models_weights models_weights/

CMD uvicorn api.fast:app --port=$PORT --host=0.0.0.0
