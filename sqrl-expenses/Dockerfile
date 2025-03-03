FROM python:3.12-slim
WORKDIR /app

COPY . .

# Verify the file exists after copying (this will show in build logs)
RUN ls -la && \
    echo "Checking for squirrels.yml:" && \
    ls -la squirrels.yml || echo "squirrels.yml not found!"

RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4465

CMD ["sqrl", "run", "--host", "0.0.0.0", "--port", "4465"]
