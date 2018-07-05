FROM python:3.5

COPY requires.txt /root/
RUN pip install -r /root/requires.txt

COPY api /opt/

CMD python /opt/api.py