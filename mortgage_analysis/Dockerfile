FROM python:3.12-slim
WORKDIR /app

COPY ./requirements.lock .
COPY ./mortgage_analysis/ .

# Only needed if any python dependencies are installed from git, or for the
# "sqrl deps" command if there are packages defined in "squirrels.yml"
RUN apt-get update && apt-get install -y git

RUN pip install --no-cache-dir -r requirements.lock

CMD ["sqrl", "run", "--host", "0.0.0.0"]
