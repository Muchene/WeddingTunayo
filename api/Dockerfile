FROM python:3.8 


WORKDIR /opt/api/
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/opt/api/"
CMD ["/opt/api/api.py"]