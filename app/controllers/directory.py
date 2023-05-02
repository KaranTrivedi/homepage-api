from litestar import Controller, get, post

# from litestar.partial import Partial

from app.models.directory import Dirobject
from app.views import directory

from logging import getLogger

logger = getLogger(__name__)

class DirectoryController(Controller):
    path = "/directory"

    @get("/folder/{path:path}")
    async def get_dirobjects(self, path: str) -> Dirobject:
        """
        Returns list of files and folders for a given filepath.

        Args:
            path (str): _description_

        Returns:
            Dirobject: _description_
        """

        logger.info(path)

        return directory.dirobjects(path)
