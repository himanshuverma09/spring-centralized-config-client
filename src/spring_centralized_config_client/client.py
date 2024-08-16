import requests
from requests.auth import HTTPBasicAuth

CIPHER = "{cipher}"


class SpringCentralizedConfigClient:
    def __init__(
        self,
        app_name=None,
        profile='dev',
        branch='main',
        url='localhost:9000',
        auth_required=False,
        username='',
        password='',
        decrypt=False,
    ) -> None:
        self._app_name = app_name
        self._profile = profile
        self._branch = branch
        self._url = url
        self._auth_required = auth_required
        self._username = username
        self._password = password
        self._decrypt = decrypt

    def get_config(self):
        request_url = f"{self._url}/{self._app_name}/{self._profile}/{self._branch}"
        if self._auth_required:
            r = requests.get(request_url, auth=HTTPBasicAuth(
                self._username, self._password))
        else:
            r = requests.get(request_url)
        if r.status_code == 200:
            config_json = r.json()
            config = config_json["propertySources"][0]["source"]
            if self._decrypt:
                config = self._decrypt_config(config)
            return config
        else:
            raise Exception(
                "Failed to get configuration",
                f"HTTP Response Code : {r.status_code}",
            )

    def _decrypt_config(self, config):
        for key in config:
            if CIPHER in config[key]:
                config[key] = self._fetch_decrypted_config(
                    config[key].replace("{cipher}", ""))
        return config

    def _fetch_decrypted_config(self, payload):
        request_url = f"{self._url}/decrypt/"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(request_url, auth=HTTPBasicAuth(
            self._username, self._password), data=payload, headers=headers)
        if r.status_code == 200:
            return r.text
        else:
            raise Exception(
                "Failed to get decrypted key",
                f"HTTP Response Code : {r.status_code}",
            )
