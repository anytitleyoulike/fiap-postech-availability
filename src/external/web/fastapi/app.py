from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.external.web.fastapi.api.api import router as api_router
from src.config import get_config
from src.external.web.fastapi.exception_handler import register_exceptions

config = get_config()


app = FastAPI(
    title=config.TITLE,
    version=config.VERSION,
    docs_url=config.DOCS_URL,
    redoc_url=config.REDOC_URL,
    openapi_url=config.OPENAPI_URL,
    root_path=config.ROOT_PATH,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

register_exceptions(app)
