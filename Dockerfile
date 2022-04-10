FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py migrate
COPY . .
EXPOSE 8000
