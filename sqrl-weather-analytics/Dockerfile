FROM python:3.12-slim
WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4465 

CMD ["sqrl", "run", "--host", "0.0.0.0", "--port", "4465"]
