FROM python:3.9

COPY . /app
WORKDIR /app

# https://jh-industry.tistory.com/34
# https://stynxh.github.io/2019-10-09-Set-Selenium-and-Chrome-browser-in-Docker-korean/

RUN apt-get -y update
RUN apt-get install wget
RUN apt-get install unzip  
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt-get -y install ./google-chrome-stable_current_amd64.deb

# CHROME
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/goodle.list'
RUN apt-get update
RUN apt-get install -y google-chrome-stable

# install python package
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "run.py"]