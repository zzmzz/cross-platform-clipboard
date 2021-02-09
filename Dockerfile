# python:alpine is 3.{latest}
FROM python:alpine

LABEL maintainer="Steven Zhu"

RUN pip install flask

COPY src /src/

EXPOSE 8080

ENTRYPOINT ["python", "/src/app.py"]