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
docker-compose -f docker-compose-local.yml up -d
```

When you first navigate to https://localhost in your browser, you'll get a security warning. You can:
1. Click "Advanced" and then "Proceed to localhost (unsafe)"
2. Or, add the certificate to your trusted root certificates:
    - Export the certificate from your browser
    - Open "Manage computer certificates" from Windows search
    - Navigate to "Trusted Root Certification Authorities" → "Certificates"
    - Right-click → "All Tasks" → "Import" and follow the wizard

### EC2 Instance Setup

First, install Docker and Docker Compose:
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html
- https://stackoverflow.com/questions/63708035/installing-docker-compose-on-amazon-ec2-linux-2-9kb-docker-compose-file

Next, copy the following volume files:
- sqrl-weather-analytics/.env.local → ~/volumes/sqrl-weather-analytics/.env.local
- sqrl-expenses/.env.local → ~/volumes/sqrl-expenses/.env.local

To use a custom domain name like "subdomain.duckdns.org", you'll need to:

1. Create a `duckdns.ini` file in the root directory with the following content:

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
