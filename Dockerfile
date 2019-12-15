FROM python

LABEL Author="Laurentiu Pop"
LABEL E-mail="laur.pop.91@gmail.com"
LABEL version="0.0.1"

ENV FLASK_APP "server.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /project
WORKDIR /project

ADD . /project

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

WORKDIR /project/app
CMD flask run --host=0.0.0.0