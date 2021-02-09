# python:alpine is 3.{latest}
FROM python:alpine

LABEL maintainer="Steven Zhu"

RUN pip install flask

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]