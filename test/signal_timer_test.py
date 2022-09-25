from pytest import fixture, raises
from subprocess import run
from requests import post, exceptions
from json import load
from time import sleep
import math

post_address = "http://0.0.0.0:80/"

# Data which will start the timing process
start_timing_input_file_path = "test/assets/start_timing_input.json"
start_timing_input_file = open(start_timing_input_file_path)
start_timing_input_data = load(start_timing_input_file)


# Data which will complete the timing process
complete_timing_input_file_path = "test/assets/complete_timing_input.json"

complete_timing_expected_output_file_path = (
    "test/assets/complete_timing_expected_output.json"
)

listener1_output_file_path = "test/artifacts/listener1_output.json"
listener2_output_file_path = "test/artifacts/listener2_output.json"

complete_timing_input_file = open(complete_timing_input_file_path)
complete_timing_input_data = load(complete_timing_input_file)

complete_timing_expected_output_file = open(complete_timing_expected_output_file_path)
complete_timing_expected_data = load(complete_timing_expected_output_file)


@fixture
def start_stop_containers():
    run(["docker-compose", "-f", "test/docker-compose.test.yml", "up", "-d", "--build"])

    # sleep is required here as there is a delay between the execution of the command and the containers actually being responsive
    sleep(1)

    yield
    run(["docker-compose", "-f", "test/docker-compose.test.yml", "down"])


def test_container_pipeline(start_stop_containers):
    start_timing_response = post(url=post_address, json=start_timing_input_data)
    sleep(1)

    assert start_timing_response.status_code == 200
    assert start_timing_response.text == "OK - data accepted"

    # sleep to let some time pass for the `signal-timer` to record elapsed time
    sleep(1)

    complete_timing_response = post(url=post_address, json=complete_timing_input_data)
    sleep(1)

    assert complete_timing_response.status_code == 200

    listener1_output_file = open(listener1_output_file_path)
    listener1_output_data = load(listener1_output_file)

    listener2_output_file = open(listener2_output_file_path)
    listener2_output_data = load(listener2_output_file)

    # We do not assert the timestamp because we cannot mock the value to ensure consistency across the board
    # we round elapsed time for consistency
    assert (
        math.trunc(listener1_output_data["time_passed"])
        == math.trunc(listener2_output_data["time_passed"])
        == complete_timing_expected_data["time_passed"]
    )


def test_wrong_address(start_stop_containers):
    with raises(exceptions.ConnectionError):
        post(url="http://signal_timer_test_container", json=start_timing_input_data)


def test_wrong_port(start_stop_containers):
    with raises(exceptions.ConnectionError):
        post(url="http://0.0.0.0:9090/", json=start_timing_input_data)
