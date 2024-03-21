FROM python:latest
WORKDIR /app

COPY loggerManager.py /app/loggerManager.py
COPY ImmichAutoAlbum.py /app/ImmichAutoAlbum.py
COPY immichAPI.py /app/immichAPI.py

COPY config.json /app/config.json
COPY requirements.txt /app/requirements.txt
COPY crontab /etc/cron.d/crontab

RUN apt-get update && apt-get -y install cron && \
    pip3 install -r /app/requirements.txt && \
    chmod 0644 /etc/cron.d/crontab && \
    /usr/bin/crontab /etc/cron.d/crontab

#uncoment this line if you want it to do an update on build
#RUN /usr/local/bin/python3 /app/ImmichAutoAlbum.py

CMD ["cron", "-f"]