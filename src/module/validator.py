"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""
import time
import datetime

from logging import getLogger
from module.params import PARAMS

log = getLogger("validator")


def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        allowed_data_types = [dict]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"

        if not isinstance(data[PARAMS["INPUT_LABEL"]], (float, int)):
            return f"Detected type: {type(data[PARAMS['INPUT_LABEL']])} | Must be real number | invalid!"

        if not isinstance(data[PARAMS["TIMESTAMP"]], (int)):
            return "timestamp expected as integer value"

        if data[PARAMS["TIMESTAMP"]] < 0:
            return "timestamp expected as a non-negative integer"

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"
