FROM python:3.9.13

RUN mkdir /app

VOLUME /app

WORKDIR /app

ADD requirements*.txt /app/

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]
