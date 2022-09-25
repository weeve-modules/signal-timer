# Signal Timer Python Processing Module

|              |                                                                  |
| ------------ | ---------------------------------------------------------------- |
| name         | Python Signal Timer Processing module                            |
| version      | v1.0.0                                                           |
| GitHub       | [python-signal-timer-processing-module](https://github.com/barrage/signal-timer) |
| authors      | Denis Pilon, Bruno Lipovac                                       |

***
## Table of Content

- [Python Signal Timer Processing Module](#python-signal-timer-processing-module)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Module Variables](#module-variables)
  - [Module Testing](#module-testing)
  - [Dependencies](#dependencies)
***

## Description 

This is a Python Processing module which is a basic signal duration timer. It monitors the input
and starts a counter measuring the duration that the signal keeps or exceeds a certain
value.

## Module Variables

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)    |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received               |
| INGRESS_PORT          | string | Port to which data will be received               |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module            |
| INPUT_LABEL           | string | Label of the monitored signal e.g. temperature    |
| TIMESTAMP             | string | Key of the input object to access the timestamp value |
| CONDITION             | enum | Allowed conditions: `No condition`, `(==) equal to`, `(!=) not equal to`, `(>) greater than`, `(>=) greater than or equal to`, `(<) less than`, `(<=) less than or equal to` |
| COMPARE_VALUE         | float  | Value to compare to in order to start the signal duration timing
| OUTPUT_UNIT           | enum | Determines the conversion of the signal duration. Allowed units: `ms`, `s`, `min`, `hrs` |
| OUTPUT_LABEL          | string | Label of the output object for the signal duration value e.g. `time_passed` | 

## Module Testing

To test module navigate to `test` directory. In `test/assets` edit both .json file to provide input for the module and expected output. During a test, data received from the listeners are compared against expected output data. You can run tests with `make run_test`.

## Dependencies

The following are module dependencies:

* bottle
* requests

The following are developer dependencies:

* pytest
* flake8
* black

## Input

Input to this module is JSON body single object, key of the triggering value must be the same as the environment variable value specified in the module environment:

Example of single object:


```json
{
  "<INPUT_LABEL>": 15,
  "timestamp": 1659527972657
}
```

Example when INPUT_LABEL is set to `temperature`:

```json
{
  "temperature": 15,
  "timestamp": 1659527972657
}
```


## Output
Output of this module is an object containing signal duration in the unit of time specified by the module environment variable and a timestamp for tracking purposes:

```json
{
  "<OUTPUT_LABEL>": 100,
  "timestamp": 1659527972757
}
```

Example when OUTPUT_LABEL is set to `signal_duration_in_seconds`:

```json
{
  "signal_duration_in_seconds": 100,
  "timestamp": 1659527972757
}
```