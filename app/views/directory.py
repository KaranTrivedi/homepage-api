"""
Functions for fetching directory related information.
"""

from app.models.directory import Dirobject

def dirobjects(path: str) -> Dirobject:
    """
    

    Args:
        path (str): _description_

    Returns:
        Dirobject: _description_
    """

    return {
        "files" : [],
        "folders": []
    }