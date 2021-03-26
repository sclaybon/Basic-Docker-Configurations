FROM python:3.7
EXPOSE 8001
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY voila-wrapper ./user/local/voila-wrapper
COPY . .
RUN chmod +x ./user/local/voila-wrapper
ENTRYPOINT ./user/local/voila-wrapper