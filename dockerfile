FROM python:3
RUN mkdir /data
WORKDIR /data
ADD . /data
ADD requirements.txt /data
RUN pip install -r requirements.txt
CMD python ./server.py
