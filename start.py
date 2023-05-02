#!./venv/bin/python

"""
Start file for initiating uvicorn.
"""

import configparser
import logging.config
import uvicorn

# Define config and logger.
CONFIG = configparser.ConfigParser()
CONFIG.read('conf/config.ini')
SECTION = "start"

IP = CONFIG['global']["ip"]
PORT = CONFIG['global']["port"]

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(funcName)s::%(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "use_colors": False,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "fmt": '%(asctime)s::%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            "use_colors": False,
        }
    },
    "handlers":
    {
        "default":
        {
            "formatter": "default",
            "class": 'logging.FileHandler',
            "filename": CONFIG[SECTION]["default"]
        },
        "error":
        {
            "formatter": "default",
            "class": 'logging.FileHandler',
            "filename": CONFIG[SECTION]["error"]
        },
        "access":
        {
            "class": 'logging.NullHandler'
            # "formatter": "access",
            # "class": 'logging.FileHandler',
            # "filename": CONFIG[SECTION]["access"]
        },
    },
    "loggers":
    {
        "": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "asgi-logger": {"handlers": ["default"], "level": "INFO", "propagate": False},
    }
}

def main():
    """
    Main function
    """

    uvicorn.run(
        app="app.main:app",
        host=IP,
        port=int(PORT),
        reload=True,
        log_config=LOG_CONFIG,
        log_level="info"
    )

if __name__ == "__main__":
    main()

