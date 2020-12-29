FROM python:3

WORKDIR /usr/src/app
COPY . .

RUN apt-get update 

RUN apt install -y cifs-utils

#Install wget 
RUN apt-get install -y wget 
#Install Cron
RUN apt-get -y install cron
# Add crontab file in the cron directory
COPY crontab /etc/cron.d/hello-cron
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron
# Apply cron job
RUN crontab /etc/cron.d/hello-cron

# COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]