FROM python:3

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
COPY . .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]