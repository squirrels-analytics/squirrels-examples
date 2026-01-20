from squirrels import SquirrelsProject
from pathlib import Path
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import asyncio
import uvicorn

load_dotenv(override=True)


def main():
    current_dir = Path(__file__).parent
    expenses_project_path = str(current_dir / "sqrl-expenses")
    mortgage_project_path = str(current_dir / "sqrl-mortgage-analysis")
    weather_project_path = str(current_dir / "sqrl-weather-analytics")

    # Initialize the project
    with (
        SquirrelsProject(project_path=expenses_project_path) as expenses_proj,
        SquirrelsProject(project_path=mortgage_project_path) as mortgage_proj,
        SquirrelsProject(project_path=weather_project_path) as weather_proj
    ):
        asyncio.run(expenses_proj.build())

        # Get the FastAPI components
        expenses_server = expenses_proj.get_fastapi_components()
        mortgage_server = mortgage_proj.get_fastapi_components()
        weather_server = weather_proj.get_fastapi_components()

        # Create the lifespan for the main app
        @asynccontextmanager
        async def lifespan(app: FastAPI | None = None):
            async with expenses_server.lifespan(app), mortgage_server.lifespan(app), weather_server.lifespan(app):
                yield

        # Set the app to the FastAPI app
        app = FastAPI(lifespan=lifespan)
        app.mount(expenses_server.mount_path, expenses_server.fastapi_app)
        app.mount(mortgage_server.mount_path, mortgage_server.fastapi_app)
        app.mount(weather_server.mount_path, weather_server.fastapi_app)

        # Run the app
        uvicorn.run(app)


if __name__ == "__main__":
    main()
