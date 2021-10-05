import logging

import requests
import http.client as http_client
from requests import Response


def setup_logger():
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


class APIClient:

    def __init__(self, base_address):
        self.base_address = base_address
        setup_logger()
        self.headers = {
            "X-API-Context-Shop-Id": "2527",
            "X-Data-Platform": "Android",
            "X-Data-Model": "Samsung",
            "X-Data-Version": "1.14",
            "Content-Type": "application/json",
        }

    def post(self, path="/", params=None, data=None) -> Response:
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=self.headers)

    def get(self, path="/", params=None) -> Response:
        return requests.get(url=self.base_address + path, params=params)