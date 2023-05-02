from starlite import LoggingConfig, Starlite, get, OpenAPIConfig
from starlite.middleware import LoggingMiddlewareConfig

#logging_middleware_config = LoggingMiddlewareConfig()

logging_config = LoggingConfig(
    loggers={
        "my_app": {
            "level": "INFO",
            "handlers": ["queue_listener"],
        }
    }
)

@get("/")
async def index() -> dict[str, str]:
    """
    index function
    """

    return "Hello world!"


app = Starlite(route_handlers=[index], logging_config=logging_config,
        openapi_config=OpenAPIConfig(title="My API", version="1.0.0")
    )
