# squirrels-examples

Each subfolder within this repo represents a different example of a Squirrels project.

See the README in the subfolder for descriptions of the examples and additional setup required for playing with the examples for yourself.

## Setup

Note: The steps below were tested on Python 3.14 for all project folders.

First, go into a project folder, and run:

```bash
uv sync -p 3.14
```

Activate the virtual environment and test that it works by running `squirrels -h` or `sqrl -h` to see available commands.

Go into any example / subfolder (which all should contain a `squirrels.yml` file) and run the command below to activate the API server:

```bash
sqrl run --build
```
