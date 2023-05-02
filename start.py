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

def main():
    """
    Main function
    """

    # logging.basicConfig(
    #     filename=CONFIG[SECTION]["default"],
    #     level=CONFIG[SECTION]["level"],
    #     format="%(asctime)s::%(levelname)s::%(name)s::%(funcName)s::%(message)s",
    #     datefmt="%Y-%m-%dT%H:%M:%S%z",
    # )

    uvicorn.run(
        app="app.main:app",
        host=IP,
        port=int(PORT),
        reload=False,
    )

if __name__ == "__main__":
    main()

