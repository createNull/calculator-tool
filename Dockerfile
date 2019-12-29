FROM python:3.8-slim

LABEL Author="Laurentiu Pop"
LABEL E-mail="laur.pop.91@gmail.com"
LABEL version="0.0.1"

ENV FLASK_APP "server.py"
ENV FLASK_ENV "development"

RUN git clone https://github.com/createNull/calculator-tool.git && \
    cd calculator-tool && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

WORKDIR /calculator-tool/app

CMD flask run --host=0.0.0.0