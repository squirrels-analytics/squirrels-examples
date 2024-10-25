# mortgage_analysis

Sample squirrels project for mortgage analysis

## Running with Docker

To build a docker image, go to the parent directory (squirrels-examples), and run the following:

```bash
docker build -t mortgage-analysis-squirrels -f mortgage_analysis/Dockerfile .
```

You can then run your container by running this with your choice of [host-port]:

```bash
docker run --rm -t -p [host-port]:4465 mortgage-analysis-squirrels
```

Once it's running, you can access the Squirrels Testing UI by entering "localhost:[host-port]/" in your web browser.
