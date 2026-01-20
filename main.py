from squirrels import SquirrelsProject
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import uvicorn
import argparse

load_dotenv()


def main(host: str, port: int):
    current_dir = Path(__file__).parent
    index_html_path = current_dir / "index.html"
    expenses_project_path = str(current_dir / "sqrl-expenses")
    mortgage_project_path = str(current_dir / "sqrl-mortgage-analysis")
    weather_project_path = str(current_dir / "sqrl-weather-analytics")
    host_for_banner = host if host != "0.0.0.0" else "localhost"

    with (
        SquirrelsProject(project_path=expenses_project_path) as expenses_proj,
        SquirrelsProject(project_path=mortgage_project_path) as mortgage_proj,
        SquirrelsProject(project_path=weather_project_path) as weather_proj,
    ):
        expenses_server = expenses_proj.get_fastapi_components(host=host_for_banner, port=port)
        mortgage_server = mortgage_proj.get_fastapi_components(host=host_for_banner, port=port)
        weather_server = weather_proj.get_fastapi_components(host=host_for_banner, port=port)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            """
            Build and merge lifespans of multiple Squirrels projects under one FastAPI app.
            
            Currently, only the expenses project requires building.
            """
            await expenses_proj.build()

            async with (
                expenses_server.lifespan(app), 
                mortgage_server.lifespan(app),
                weather_server.lifespan(app),
            ):
                yield

        app = FastAPI(lifespan=lifespan)
        app.mount(expenses_server.mount_path, expenses_server.fastapi_app)
        app.mount(mortgage_server.mount_path, mortgage_server.fastapi_app)
        app.mount(weather_server.mount_path, weather_server.fastapi_app)

        @app.get("/")
        async def root():
            def _href(mount_path: str) -> str:
                return mount_path + "/studio"

            template = index_html_path.read_text(encoding="utf-8")
            html = (
                template.replace("{{EXPENSES_MOUNT_PATH}}", _href(expenses_server.mount_path))
                    .replace("{{MORTGAGE_MOUNT_PATH}}", _href(mortgage_server.mount_path))
                    .replace("{{WEATHER_MOUNT_PATH}}", _href(weather_server.mount_path))
            )
            return HTMLResponse(content=html, media_type="text/html")

        uvicorn.run(app, host=host, port=port, proxy_headers=True, forwarded_allow_ips="*")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Squirrels analytics examples server")
    parser.add_argument("--host", default="localhost", help="Host to bind the server to (default: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind the server to (default: 8000)")

    args = parser.parse_args()

    main(args.host, args.port)
