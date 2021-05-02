FROM python:3.7
EXPOSE 8001
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY streamlit-wrapper ./streamlit-wrapper
RUN chmod +x ./streamlit-wrapper
ENTRYPOINT ./streamlit-wrapper