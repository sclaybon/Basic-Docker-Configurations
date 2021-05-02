FROM python:3.7
EXPOSE 8001
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY streamlit-wrapper ./user/local/streamlit-wrapper
COPY . .
CMD [ "python", "./json_get_dashboard_name.py" ]
RUN chmod +x ./user/local/streamlit-wrapper
ENTRYPOINT ./user/local/streamlit-wrapper