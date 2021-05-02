FROM python:3.7
EXPOSE 8001
WORKDIR /usr/local/streamlit
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY streamlit-wrapper /usr/local/streamlit/streamlit-wrapper
COPY . .
RUN chmod +x /usr/local/streamlit/streamlit-wrapper
ENTRYPOINT /usr/local/streamlit/streamlit-wrapper