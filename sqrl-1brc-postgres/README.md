# Squirrels Example - 1 Billion Row Challenge with Postgres

This is an example of how to create a Squirrels project that queries 1 billion rows from Postgres.

## Setup

Requires Python 3.10 or higher.

First run `pip install -r requirements.txt` to install the dependencies.

Next, run `python createMeasurements.py` to create a `measurements.txt` file with 1 billion rows of data.

Then, in your PostgreSQL client, create a table called `weather_data` with the following DDL:

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    recorded_date DATE,
    temperature FLOAT
);
```

Load the `measurements.txt` file into the `weather_data` table using the following command.

```sql
\COPY weather_data FROM 'measurements.txt' DELIMITER ';'
```

To associate your PostgreSQL database with Squirrels, create an `env.yml` file in the current directory that looks like this:

```yaml
env_vars:
  postgres_uri: postgresql://username:password@host:5432/database
```

We can use Squirrels to build necessary data artifacts (as DuckDB files) for more performant queries. This is most efficient when the machine has between 5GB to 10GB of RAM for each core (to avoid excessive spilling to disk). To limit the number of cores used, you can create a `duckdb_init.sql` file in the current directory that looks like this:

```sql
SET threads = 4;
```

Finally, run `sqrl build` to build the data artifacts.

## Running the project

Run `sqrl run` to start the Squirrels server.

Access the Squirrels Testing UI at `http://localhost:4465/`, or the API docs at `http://localhost:4465/docs`.
