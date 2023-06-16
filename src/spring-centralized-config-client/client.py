import requests
from requests.auth import HTTPBasicAuth
from utils import make_flat_json

CIPHER = "{cipher}"

class SpringCentralizedConfigClient:
    def __init__(self, username, password, app_name, url, profile, branch) -> None:
        self._username = username
        self._password = password
        self._app_name = app_name
        self._url = url
        self._profile = profile
        self._branch = branch

    def get_config(self):
        request_url = f"{self._url}/{self._branch}/{self._app_name}-{self._profile}.json"
        r = requests.get(request_url, auth=HTTPBasicAuth(self._username, self._password))

        if r.status_code == 200:
            decrypted_config = self._decrypt_config(make_flat_json(r.json()))
            return decrypted_config
        else:
            raise Exception(
                "Failed to get configuration",
                f"HTTP Response Code : {r.status_code}",
            )

    def _decrypt_config(self, config):
        for key in config:
            if "{cipher}" in config[key]:
                config[key] = self._fetch_decrypted_config(config[key].replace("{cipher}", ""))
        return config

    def _fetch_decrypted_config(self, payload):
        request_url = f"{self._url}/decrypt/"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(request_url, auth=HTTPBasicAuth(self._username, self._password), data=payload, headers = headers)
        if r.status_code == 200:
            return r.text
        else:
            raise Exception(
                "Failed to get decrypted key",
                f"HTTP Response Code : {r.status_code}",
            )

