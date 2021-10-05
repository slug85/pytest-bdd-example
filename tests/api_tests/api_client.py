import logging
from typing import Dict

import requests
import http.client as http_client
from requests import Response

from tests.datastore import User


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
        self.client_secret = "ZlxUY81YlQOdWcof9G6EkHiz0316Z1Xhr0WNHDKY"
        self.client_id = 8
        setup_logger()
        self.headers = {
            "X-API-Context-Shop-Id": "2527",
            "X-Data-Platform": "Android",
            "X-Data-Model": "Samsung",
            "X-Data-Version": "1.14",
            "Content-Type": "application/json",
        }

    def post(self, path="/", params=None, data=None, headers=None, user: User = None) -> Response:
        url = self.base_address + path
        new_headers = self.merge_headers(headers, user)
        return requests.post(url=url, params=params, data=data, headers=new_headers)

    def get(self, path="/", params=None, headers=None, user: User = None) -> Response:

        new_headers = self.merge_headers(headers, user)
        return requests.get(url=self.base_address + path, params=params, headers=new_headers)

    def merge_headers(self, headers, user: User = None) -> Dict:
        new_headers = {}
        session_headers = dict(self.headers)
        if user and user.token:
            new_headers = {"Authorization": f"Bearer {user.token}"}
        if headers:
            new_headers.update(headers)
            new_headers.update(session_headers)
        else:
            new_headers.update(session_headers)
        return new_headers
