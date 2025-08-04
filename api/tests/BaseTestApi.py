import requests
import json
import os

#API test are not in scope for this cersion, For future purpose only
class BaseTestApi:
    def __init__(self, env="prod"):
        # Load config
        config_path = os.path.join("config", "api-config.json")
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        self.base_url = config[env]["base_url"]
        self.token = config[env].get("token", None)

        # Create a session to persist headers
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def _build_url(self, endpoint):
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def _log_response(self, response):
        print(f"\n[RESPONSE] Status: {response.status_code}")
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except Exception:
            print(response.text)

    def get(self, endpoint, params=None, headers=None):
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, headers=headers)
        self._log_response(response)
        return response

    def post(self, endpoint, body=None, params=None, headers=None):
        url = self._build_url(endpoint)
        response = self.session.post(url, params=params, json=body, headers=headers)
        self._log_response(response)
        return response

    def put(self, endpoint, body=None, params=None, headers=None):
        url = self._build_url(endpoint)
        response = self.session.put(url, params=params, json=body, headers=headers)
        self._log_response(response)
        return response

    def delete(self, endpoint, params=None, headers=None):
        url = self._build_url(endpoint)
        response = self.session.delete(url, params=params, headers=headers)
        self._log_response(response)
        return response



