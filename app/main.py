"""
Setup litestar project
"""

from litestar import Litestar, get
import logging
from typing import TYPE_CHECKING

import time

from litestar.middleware import DefineMiddleware
from asgi_logger import AccessLoggerMiddleware
from app.controllers.directory import DirectoryController
from litestar.static_files.config import StaticFilesConfig

if TYPE_CHECKING:
    from litestar.datastructures import State
    from litestar.types import Scope

logger = logging.getLogger(__name__)

LOGGING_MIDDLEWARE = DefineMiddleware(AccessLoggerMiddleware,\
                                      format='%(client_addr)s - "%(request_line)s" %(L)s %(B)s %(status_code)s',\
                                      logger=logging.getLogger("asgi-logger"))

@get("/ping")
async def ping() -> bool:
    """
    Basic ping function.
    """

    return True

def start_up() -> None:
    """
    Start Up function.
    """

    print(f"""####################################################################################\n\
{time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime())}::INFO::main.py::startup::Restarted.""")

async def after_exception_handler(exc: Exception, scope: "Scope", state: "State") -> None:
    """
    Hook function that will be invoked after each exception.
    """

    if not hasattr(state, "error_count"):
        state.error_count = 1
    else:
        state.error_count += 1

    logger.info(
        f"an exception of type {type(exc).__name__,} has occurred for requested path {scope['path']} and the application error count is {state.error_count}."
    )

app = Litestar(
        route_handlers=[
            ping,
            DirectoryController
        ],
        middleware=[
            LOGGING_MIDDLEWARE
        ],
        on_startup=[start_up],
        on_shutdown=[],
        static_files_config=[
            StaticFilesConfig(directories=["logs"], path="/logs"),
        ],
        after_exception=[after_exception_handler]
    )

