from squirrels import SquirrelsProject
from pathlib import Path
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()


current_dir = Path(__file__).parent
expenses_project_path = str(current_dir / "sqrl-expenses")
mortgage_project_path = str(current_dir / "sqrl-mortgage-analysis")
weather_project_path = str(current_dir / "sqrl-weather-analytics")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Build and run multiple Squirrels projects under one FastAPI app.

    Important:
    - Avoid calling `asyncio.run()` at import time (uvicorn/anyio manages the loop).
    - Avoid patching the event loop (`nest_asyncio`) which can break anyio internals.
    """
    with (
        SquirrelsProject(project_path=expenses_project_path) as expenses_proj,
        SquirrelsProject(project_path=mortgage_project_path) as mortgage_proj,
        SquirrelsProject(project_path=weather_project_path) as weather_proj,
    ):
        expenses_server = expenses_proj.get_fastapi_components()
        mortgage_server = mortgage_proj.get_fastapi_components()
        weather_server = weather_proj.get_fastapi_components()

        # Mount sub-apps once (in case of reloads).
        if not getattr(app.state, "_sqrl_mounted", False):
            # Build inside the server event loop (only the expenses project requires building currently).
            await expenses_proj.build()

            app.mount(expenses_server.mount_path, expenses_server.fastapi_app)
            app.mount(mortgage_server.mount_path, mortgage_server.fastapi_app)
            app.mount(weather_server.mount_path, weather_server.fastapi_app)
            app.state._sqrl_mounted = True

        async with (
            expenses_server.lifespan(app),
            mortgage_server.lifespan(app),
            weather_server.lifespan(app),
        ):
            yield


app = FastAPI(lifespan=lifespan)
