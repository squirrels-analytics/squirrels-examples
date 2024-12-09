# squirrels-examples

Each subfolder within this repo represents a different example of a Squirrels project.

See below for descriptions of the examples and the setup required for playing with the examples for yourself.

## Example Descriptions

- test_regression
    - An example project to test most Squirrels features. Also an example of creating fraud analysis datasets that accept many widget parameters.
- weather_analytics
    - An extension of the project created from the tutorial from the [official Squirrels documentation](https://squirrels-nest.github.io/docs/intro). Example of analyzing weather pattern under different time periods or conditions.

## Setup

Note: The steps below were tested on Python 3.12.5 for all project folders.

First, go into a project folder, create the virtual environment for the project, and activate it.

Then, install the squirrels framework and its dependencies.

```bash
pip install -r requirements.lock
```

Test that it works by running `squirrels -h` or `sqrl -h` to see available commands.

Go into any example / subfolder (which all should contain a `squirrels.yml` file) and run the command below to activate the API server:

```bash
sqrl run
```
