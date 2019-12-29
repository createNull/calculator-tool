FROM python

LABEL Author="Laurentiu Pop"
LABEL E-mail="laur.pop.91@gmail.com"
LABEL version="0.0.2"

RUN git clone https://github.com/createNull/calculator-tool.git && \
    cd calculator-tool && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /calculator-tool/app

ENTRYPOINT ["python"]
CMD ["server.py"]