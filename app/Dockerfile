FROM python:3.6
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py /app
COPY app.py /app
COPY config.py /app
CMD python main.py
