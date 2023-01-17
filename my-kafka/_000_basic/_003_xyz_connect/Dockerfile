FROM python:3.9-slim

WORKDIR /usr/src
RUN apt-get -y update
RUN apt install wget -y
RUN apt install unzip -y
RUN apt install curl -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN mkdir chrome
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY * ./
COPY _000_KafkaManager.py ./
COPY _002_publish_5_prod.py ./

ENTRYPOINT ["python", "_002_publish_5_prod.py"]