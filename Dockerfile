# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR  /DEPLOY-$(date +%Y-%m-%d)

COPY . ./WORKDIR

COPY requirements.txt /WORKDIR

RUN pip3 install -r ./WORKDIR/requirements.txt


# CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["docker", "images" ]