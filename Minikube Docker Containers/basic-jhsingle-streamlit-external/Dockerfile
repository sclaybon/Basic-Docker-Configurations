FROM python:3.7
EXPOSE 8001
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY streamlit-wrapper ./user/local/streamlit-wrapper
COPY . .
RUN chmod +x ./user/local/streamlit-wrapper
ENTRYPOINT ./user/local/streamlit-wrapper