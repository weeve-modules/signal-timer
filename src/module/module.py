"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""
import time
from logging import getLogger
from module.params import PARAMS

log = getLogger("module")


def no_condition():
    return True


def equal(a, b):
    return a == b


def not_equal(a, b):
    return a != b


def greater(a, b):
    return a > b


def greater_equal(a, b):
    return a >= b


def less(a, b):
    return a < b


def less_equal(a, b):
    return a <= b


comparison_conditions = {
    "No condition": no_condition,
    "(==) equal to": equal,
    "(!=) not equal to": not_equal,
    "(>) greater than": greater,
    "(>=) greater than or equal to": greater_equal,
    "(<) less than": less,
    "(<=) less than or equal to": less_equal,
}


def to_milliseconds(calculated_duration):
    return calculated_duration * 1000


def to_seconds(calculated_duration):
    return calculated_duration


def to_minutes(calculated_duration):
    return (calculated_duration) / 60


def to_hours(calculated_duration):
    return (calculated_duration) / (60 * 60)


output_unit_conditions = {
    "ms": to_milliseconds,
    "s": to_seconds,
    "min": to_minutes,
    "hrs": to_hours,
}


cached_timestamp = None


def module_main(received_data: any) -> any:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        global cached_timestamp

        if (
            comparison_conditions[PARAMS["CONDITION"]](
                received_data[PARAMS["INPUT_LABEL"]], PARAMS["COMPARE_VALUE"]
            )
            and cached_timestamp is None
        ):
            log.debug(
                "Defined signal conditions have been met, starting signal timing."
            )

            cached_timestamp = time.time()

        if (
            not comparison_conditions[PARAMS["CONDITION"]](
                received_data[PARAMS["INPUT_LABEL"]], PARAMS["COMPARE_VALUE"]
            )
            and cached_timestamp is not None
        ):
            processed_data = {
                PARAMS["OUTPUT_LABEL"]: output_unit_conditions[PARAMS["OUTPUT_UNIT"]](
                    time.time() - cached_timestamp
                ),
                PARAMS["TIMESTAMP"]: int(round(time.time() * 1000)),
            }

            cached_timestamp = None

            log.debug("Signal timing completed.")

            return processed_data, None

        return None, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
