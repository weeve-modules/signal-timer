from os import getenv

PARAMS = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "trigger_value"),
    "TIMESTAMP": getenv("TIMESTAMP", "timestamp"),
    "CONDITION": getenv("INPUT_UNIT", "(>) greater than"),
    "COMPARE_VALUE": float(getenv("COMPARE_VALUE", "0")),
    "OUTPUT_UNIT": getenv("OUTPUT_UNIT", "ms"),
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "time_passed"),
}
