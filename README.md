# squirrels-examples

Each subfolder within this repo represents a different example of a Squirrels project.

See the README in the subfolder for descriptions of the examples and additional setup required for playing with the examples for yourself.

## Setup

Note: The steps below were tested on Python 3.12.5 for all project folders.

First, go into a project folder, create the virtual environment for the project, and activate it.

Then, install the squirrels framework and its dependencies.

```bash
pip install -r requirements.txt
```

Test that it works by running `squirrels -h` or `sqrl -h` to see available commands.

Go into any example / subfolder (which all should contain a `squirrels.yml` file) and run the command below to activate the API server:

```bash
sqrl run
```

The following project folders support deployment with Docker:
- sqrl-mortgage-analysis

The following project folders will support deployment with Docker soon:
- sqrl-expenses
- sqrl-weather-analytics

### Testing with Docker on a Local Machine

First, create a directory for your certificates: 

```bash
mkdir C:/nginx-certs
```

You can generate self-signed certificates using OpenSSL. If you don't have OpenSSL installed, you can use Docker to generate them:

```bash
docker run --rm -v C:/nginx-certs:/certs alpine/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /certs/privkey.pem -out /certs/fullchain.pem -subj "/CN=localhost"
```

Now you can run locally with:

```bash
cd <project-folder>
docker-compose -f docker-compose-local.yml build
docker-compose -f docker-compose-local.yml up -d
```

When you first navigate to https://localhost in your browser, you'll get a security warning. You can:
1. Click "Advanced" and then "Proceed to localhost (unsafe)"
2. Or, add the certificate to your trusted root certificates:
    - Export the certificate from your browser
    - Open "Manage computer certificates" from Windows search
    - Navigate to "Trusted Root Certification Authorities" → "Certificates"
    - Right-click → "All Tasks" → "Import" and follow the wizard

Suppose the project name and version is "mortgage/v1". You can navigate to the API docs at "https://localhost/api/squirrels-v0/project/mortgage/v1/docs".

### EC2 Instance Setup

First, install Docker, Docker Compose, and Crontab:
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html
- https://stackoverflow.com/questions/63708035/installing-docker-compose-on-amazon-ec2-linux-2-9kb-docker-compose-file
- https://jainsaket-1994.medium.com/installing-crontab-on-amazon-linux-2023-ec2-98cf2708b171

Next, clone the repo and copy the .env file to the project subfolder:
- <project-subfolder>/.env → ~/squirrels-examples/<project-subfolder>/.env

To use a custom domain name like "subdomain.duckdns.org", you'll need to:

1. Create a `duckdns.ini` file in the home directory with the following content:

```
dns_duckdns_token=<your-duckdns-token>
```

2. Run the following command to generate the certificates:

```bash
docker run -v "/etc/letsencrypt:/etc/letsencrypt" -v "/var/log/letsencrypt:/var/log/letsencrypt" -v "./duckdns.ini:/conf/duckdns.ini" infinityofspace/certbot_dns_duckdns:latest \
   certonly \
     --non-interactive \
     --agree-tos \
     --email <your-email> \
     --preferred-challenges dns \
     --authenticator dns-duckdns \
     --dns-duckdns-credentials /conf/duckdns.ini \
     --dns-duckdns-propagation-seconds 60 \
     -d "<subdomain.duckdns.org>"
```

More info can be found here: https://pypi.org/project/certbot-dns-duckdns/

3. For security, it is recommended to create a `dhparams.pem` file as such:

```bash
sudo openssl dhparam -out /etc/letsencrypt/dhparams.pem 2048
```

4. Create a cron job to renew the certificates:

Write the following contents to the `/etc/crontab` file:

```bash
24 2 * * * touch /home/ec2-user/cron.start; docker run --rm -v "/etc/letsencrypt:/etc/letsencrypt" -v "/var/log/letsencrypt:/var/log/letsencrypt" -v "/home/ec2-user/duckdns.ini:/conf/duckdns.ini" infinityofspace/certbot_dns_duckdns:latest  renew; touch /home/ec2-user/cron.end
```

The `cron.start` and `cron.end` files can be used to check if the cron job ran successfully.
