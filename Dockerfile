FROM python:3.8-slim

WORKDIR /app

ADD ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

ADD ./app/batch/load_data.py .
ADD ./app/batch/build_tokenized_text.py .
ADD ./app/batch/build_inverted_index.py .

RUN python3 load_data.py
RUN python3 build_tokenized_text.py
RUN python3 build_inverted_index.py
