#!/usr/bin/python
# Copyright 2016 Mender Software AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

def pytest_addoption(parser):
    parser.addoption("--api", action="store", default="0.1.0", help="API version used in HTTP requests")
    parser.addoption("--host", action="store", default="localhost", help="host running API")
    parser.addoption("--devices", action="store", default="1001", help="# of devices to test with")


def pytest_configure(config):
    api_version = config.getoption("api")
    host = config.getoption("host")
    test_device_count = int(config.getoption("devices"))

