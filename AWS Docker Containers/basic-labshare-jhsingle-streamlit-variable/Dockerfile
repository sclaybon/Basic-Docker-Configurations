FROM python:3.7
EXPOSE 8001
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY streamlit-wrapper ./usr/local/streamlit-wrapper
COPY . .
CMD [ "python", "./json_get_dashboard_name.py" ]
RUN chmod +x ./usr/local/streamlit-wrapper
ENTRYPOINT ./usr/local/streamlit-wrapper