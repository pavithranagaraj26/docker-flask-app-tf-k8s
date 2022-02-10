FROM python:alpine3.15

RUN pip3 install flask

ADD . /code/

CMD ["python3", "/code/app.py"]