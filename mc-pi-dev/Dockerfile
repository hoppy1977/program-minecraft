FROM python:3.9

WORKDIR /usr/src/app

RUN git clone https://github.com/py3minepi/py3minepi && pip install --no-cache-dir py3minepi/ && rm -fr py3minepi

#CMD [ "python" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]