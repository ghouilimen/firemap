FROM osgeo/gdal:ubuntu-small-latest
RUN apt-get install python3
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3","manage.py", "runserver", "0.0.0.0:8000"]