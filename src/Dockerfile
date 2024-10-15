FROM python:3.12-alpine
LABEL authors="crusazer"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod a+x /app/start.sh
EXPOSE 8000

CMD /app/start.sh