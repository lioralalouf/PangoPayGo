import json
import pathlib

class BaseTest:
    driver = None
    env = None

    def setup_method(self, method):
        self.base_url = self.get_base_url(self.env)
        print(f"\n[INFO] Environment: {self.env} | Base URL: {self.base_url}")
        self.driver.get(self.base_url)

    def get_base_url(self, env):
        root_dir = pathlib.Path(__file__).resolve().parents[2]
        config_path = root_dir / "config" / "config.json"

        if not config_path.exists():
            raise FileNotFoundError(f"[ERROR] config.json not found at: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        if env not in config:
            raise Exception(f"[ERROR] Environment '{env}' not found in config.json")

        return config[env]["base_url"]
