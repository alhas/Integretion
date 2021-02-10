FROM python:3.8.3
MAINTAINER alhas bahtiyaralialhas@gmail.com

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY service/ ./service
COPY app.py .

CMD ["python","./app.py"]



