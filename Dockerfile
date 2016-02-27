FROM python:3.4
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y \
    gettext  \
    libgdal-dev
RUN mkdir ~/.pip/
RUN pip install \
    -r requirements/local.txt
EXPOSE 3010
