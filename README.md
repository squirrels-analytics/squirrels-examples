# squirrels-examples

Each subfolder within this repo represents a different example of a Squirrels project. The current examples are:
- sqrl-expenses
- sqrl-expenses-slim
- sqrl-mortgage-analysis
- sqrl-weather-analytics

See the README in the subfolder for descriptions of the examples and additional setup required for playing with the examples for yourself.

The main.py file in the root of the repo is a simple example of how to run multiple Squirrels projects in a single FastAPI app.

## Setup for single project

First, go into the project subfolder, and run:

```bash
uv sync -p 3.14
```

Activate the virtual environment and test that it works by running `squirrels -h` or `sqrl -h` to see available commands.

If a `.env.example` file exists, copy it to a `.env` file, and set the appropriate environment variables. See the README in the subfolder for more details if needed.

Finally, run the command below to activate the API server:

```bash
sqrl run --build
```

## Running the main.py file

Before running the main.py file, copy the `.env.example` file to a `.env` file, and set the appropriate environment variables. This step can be optional if you've already created a `.env` file in each project's subfolder.

Then, simply run:

```bash
uv run main.py
```
