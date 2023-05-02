"""
Setup litestar project
"""

from litestar import Litestar, get
import logging
from litestar.middleware import DefineMiddleware
from asgi_logger import AccessLoggerMiddleware
from app.controllers.directory import DirectoryController

LOGGING_MIDDLEWARE = DefineMiddleware(AccessLoggerMiddleware, format='%(client_addr)s - "%(request_line)s" %(L)s %(B)s %(status_code)s', logger=logging.getLogger("asgi-logger"))

@get("/ping")
async def ping() -> bool:
    """
    Basic ping function.
    """

    return True

app = Litestar(
        route_handlers=[
            ping,
            DirectoryController
            ],
        middleware=[
            LOGGING_MIDDLEWARE
        ]
    )

