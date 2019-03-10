FROM ubuntu:18.04

EXPOSE 8080

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/rolemanage/requirements.txt

WORKDIR /app/rolemanage

RUN pip3  install -r requirements.txt
RUN pip3 install gunicorn
RUN pip3 install gevent


COPY . .

CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py" , "app:app"]
